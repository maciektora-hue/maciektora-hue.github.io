import json
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def _col_idx(ref):
    m = re.match(r"[A-Z]+", ref or "A1")
    n = 0
    for ch in m.group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def _read_rows(path):
    ns = {"m": MAIN_NS, "p": PKG_REL_NS}
    with ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = ["".join(t.text or "" for t in item.iterfind(".//m:t", ns)) for item in root.findall("m:si", ns)]
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        sheet = wb.find("m:sheets", ns)[0]
        rid = sheet.attrib[f"{{{REL_NS}}}id"]
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", ns)}
        target = targets[rid]
        sheet_path = target.lstrip("/") if target.startswith("/") else "xl/" + target.lstrip("./")
        root = ET.fromstring(z.read(sheet_path))
        rows = []
        for row in root.findall(".//m:sheetData/m:row", ns):
            vals = {}
            for cell in row.findall("m:c", ns):
                i = _col_idx(cell.attrib.get("r", "A1"))
                typ = cell.attrib.get("t")
                v = cell.find("m:v", ns)
                inline = cell.find("m:is", ns)
                value = ""
                if typ == "s" and v is not None:
                    value = shared[int(v.text)]
                elif typ == "inlineStr" and inline is not None:
                    value = "".join(t.text or "" for t in inline.iterfind(".//m:t", ns))
                elif v is not None:
                    value = v.text or ""
                vals[i] = value.strip()
            if vals:
                arr = [""] * (max(vals) + 1)
                for i, value in vals.items():
                    arr[i] = value
                rows.append(arr)
    width = max((len(r) for r in rows), default=0)
    return [r + [""] * (width - len(r)) for r in rows]


def when_ready(server):
    if os.environ.get("SOL_INSPECT_ISLAND_XLSX") != "1":
        return
    root = Path(__file__).resolve().parent.parent / "dane-robocze" / "csv-tsv" / "piosenki"
    for filename in ["Glebi 2.xlsx", "Swiatla.xlsx", "Ruchu.xlsx", "Peryferia.xlsx"]:
        rows = _read_rows(root / filename)
        headers = [x.strip().lower() for x in rows[0]] if rows else []
        idx = {h: i for i, h in enumerate(headers)}
        id_col = idx.get("id")
        ids = [r[id_col].strip() for r in rows[1:] if id_col is not None and r[id_col].strip()]
        blank_id_rows = [n for n, r in enumerate(rows[1:], start=2) if id_col is not None and not r[id_col].strip()]
        payload = {
            "file": filename,
            "headers": headers,
            "positions": max(len(rows) - 1, 0),
            "nonblank_ids": len(ids),
            "distinct_ids": len(set(ids)),
            "blank_id_rows": blank_id_rows,
            "first8": rows[1:9],
            "last3": rows[-3:],
        }
        print("ISLAND_XLSX_RAW " + json.dumps(payload, ensure_ascii=False, sort_keys=True), flush=True)
