-- tabela: content_keyword_terms
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS content_keyword_terms (
    keyword_id INTEGER PRIMARY KEY,
    concept_id INTEGER NOT NULL,
    lang TEXT NOT NULL,
    keyword TEXT NOT NULL,
    keyword_norm TEXT NOT NULL,
    is_preferred INTEGER NOT NULL DEFAULT 1, maciek_neologism INTEGER CHECK (maciek_neologism IS NULL OR maciek_neologism = 1),

    FOREIGN KEY (concept_id)
        REFERENCES content_keyword_concepts(concept_id),

    CHECK (lang IN ('pl', 'en')),
    CHECK (is_preferred IN (0, 1)),

    UNIQUE (concept_id, lang, keyword_norm)
);

INSERT INTO content_keyword_terms VALUES(1,1,'pl','AA','aa',1,NULL);

INSERT INTO content_keyword_terms VALUES(2,1,'en','Alcoholics Anonymous','alcoholics anonymous',1,NULL);

INSERT INTO content_keyword_terms VALUES(3,2,'pl','abstrakcja','abstrakcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(4,2,'en','abstraction','abstraction',1,NULL);

INSERT INTO content_keyword_terms VALUES(5,3,'pl','absurd','absurd',1,NULL);

INSERT INTO content_keyword_terms VALUES(6,3,'en','absurdity','absurdity',1,NULL);

INSERT INTO content_keyword_terms VALUES(7,4,'pl','adaptacja społeczna','adaptacja społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(8,4,'en','social adaptation','social adaptation',1,NULL);

INSERT INTO content_keyword_terms VALUES(9,5,'pl','akceptacja neuroróżnorodności','akceptacja neuroróżnorodności',1,NULL);

INSERT INTO content_keyword_terms VALUES(10,5,'en','neurodiversity acceptance','neurodiversity acceptance',1,NULL);

INSERT INTO content_keyword_terms VALUES(11,6,'pl','aktywizacja behawioralna','aktywizacja behawioralna',1,NULL);

INSERT INTO content_keyword_terms VALUES(12,6,'en','behavioral activation','behavioral activation',1,NULL);

INSERT INTO content_keyword_terms VALUES(13,7,'pl','aleksytymia','aleksytymia',1,NULL);

INSERT INTO content_keyword_terms VALUES(14,7,'en','alexithymia','alexithymia',1,NULL);

INSERT INTO content_keyword_terms VALUES(15,8,'pl','alokacja','alokacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(16,8,'en','allocation','allocation',1,NULL);

INSERT INTO content_keyword_terms VALUES(17,9,'pl','analiza kontekstu','analiza kontekstu',1,NULL);

INSERT INTO content_keyword_terms VALUES(18,9,'en','context analysis','context analysis',1,NULL);

INSERT INTO content_keyword_terms VALUES(19,10,'pl','anhedonia','anhedonia',1,NULL);

INSERT INTO content_keyword_terms VALUES(20,10,'en','anhedonia','anhedonia',1,NULL);

INSERT INTO content_keyword_terms VALUES(21,11,'pl','antymateria','antymateria',1,NULL);

INSERT INTO content_keyword_terms VALUES(22,11,'en','antimatter','antimatter',1,NULL);

INSERT INTO content_keyword_terms VALUES(23,12,'pl','antyskuteczność','antyskuteczność',1,NULL);

INSERT INTO content_keyword_terms VALUES(24,12,'en','counterproductivity','counterproductivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(25,13,'pl','Apple','apple',1,NULL);

INSERT INTO content_keyword_terms VALUES(26,13,'en','Apple','apple',1,NULL);

INSERT INTO content_keyword_terms VALUES(27,14,'pl','arbiter prawdy','arbiter prawdy',1,NULL);

INSERT INTO content_keyword_terms VALUES(28,14,'en','truth arbiter','truth arbiter',1,NULL);

INSERT INTO content_keyword_terms VALUES(29,15,'pl','architektura','architektura',1,NULL);

INSERT INTO content_keyword_terms VALUES(30,15,'en','architecture','architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(31,16,'pl','architektura informacji','architektura informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(32,16,'en','information architecture','information architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(33,17,'pl','architektura pamięci','architektura pamięci',1,NULL);

INSERT INTO content_keyword_terms VALUES(34,17,'en','memory architecture','memory architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(35,18,'pl','architektura poznawcza','architektura poznawcza',1,NULL);

INSERT INTO content_keyword_terms VALUES(36,18,'en','cognitive architecture','cognitive architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(37,19,'pl','architektura systemu','architektura systemu',1,NULL);

INSERT INTO content_keyword_terms VALUES(38,19,'en','system architecture','system architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(39,20,'pl','architektura wiedzy','architektura wiedzy',1,NULL);

INSERT INTO content_keyword_terms VALUES(40,20,'en','knowledge architecture','knowledge architecture',1,NULL);

INSERT INTO content_keyword_terms VALUES(41,21,'pl','asertywność','asertywność',1,NULL);

INSERT INTO content_keyword_terms VALUES(42,21,'en','assertiveness','assertiveness',1,NULL);

INSERT INTO content_keyword_terms VALUES(43,22,'pl','asymetria relacyjna','asymetria relacyjna',1,NULL);

INSERT INTO content_keyword_terms VALUES(44,22,'en','relational asymmetry','relational asymmetry',1,NULL);

INSERT INTO content_keyword_terms VALUES(45,23,'pl','atrybucja','atrybucja',1,NULL);

INSERT INTO content_keyword_terms VALUES(46,23,'en','attribution','attribution',1,NULL);

INSERT INTO content_keyword_terms VALUES(47,24,'pl','atypowe przetwarzanie bólu','atypowe przetwarzanie bólu',1,NULL);

INSERT INTO content_keyword_terms VALUES(48,24,'en','atypical pain processing','atypical pain processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(49,25,'pl','automatyzacja pamięci','automatyzacja pamięci',1,NULL);

INSERT INTO content_keyword_terms VALUES(50,25,'en','memory automation','memory automation',1,NULL);

INSERT INTO content_keyword_terms VALUES(51,26,'pl','autonomia','autonomia',1,NULL);

INSERT INTO content_keyword_terms VALUES(52,26,'en','autonomy','autonomy',1,NULL);

INSERT INTO content_keyword_terms VALUES(53,27,'pl','bariery diagnostyczne','bariery diagnostyczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(54,27,'en','diagnostic barriers','diagnostic barriers',1,NULL);

INSERT INTO content_keyword_terms VALUES(55,28,'pl','bariery wykonawcze','bariery wykonawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(56,28,'en','executive-function barriers','executive-function barriers',1,NULL);

INSERT INTO content_keyword_terms VALUES(57,29,'pl','Bell Labs','bell labs',1,NULL);

INSERT INTO content_keyword_terms VALUES(58,29,'en','Bell Labs','bell labs',1,NULL);

INSERT INTO content_keyword_terms VALUES(59,30,'pl','bezpieczny workflow','bezpieczny workflow',1,NULL);

INSERT INTO content_keyword_terms VALUES(60,30,'en','safe workflow','safe workflow',1,NULL);

INSERT INTO content_keyword_terms VALUES(61,31,'pl','bezstronność','bezstronność',1,NULL);

INSERT INTO content_keyword_terms VALUES(62,31,'en','impartiality','impartiality',1,NULL);

INSERT INTO content_keyword_terms VALUES(63,32,'pl','bias poznawczy','bias poznawczy',1,NULL);

INSERT INTO content_keyword_terms VALUES(64,32,'en','cognitive bias','cognitive bias',1,NULL);

INSERT INTO content_keyword_terms VALUES(65,33,'pl','bimodalność mówienia','bimodalność mówienia',1,NULL);

INSERT INTO content_keyword_terms VALUES(66,33,'en','bimodal speech pattern','bimodal speech pattern',1,NULL);

INSERT INTO content_keyword_terms VALUES(67,34,'pl','bliscy','bliscy',1,NULL);

INSERT INTO content_keyword_terms VALUES(68,34,'en','significant others','significant others',1,NULL);

INSERT INTO content_keyword_terms VALUES(69,35,'pl','bliskość','bliskość',1,NULL);

INSERT INTO content_keyword_terms VALUES(70,35,'en','intimacy','intimacy',1,NULL);

INSERT INTO content_keyword_terms VALUES(71,36,'pl','blokada wykonawcza','blokada wykonawcza',1,NULL);

INSERT INTO content_keyword_terms VALUES(72,36,'en','executive shutdown','executive shutdown',1,NULL);

INSERT INTO content_keyword_terms VALUES(73,37,'pl','błąd AI','błąd ai',1,NULL);

INSERT INTO content_keyword_terms VALUES(74,37,'en','AI error','ai error',1,NULL);

INSERT INTO content_keyword_terms VALUES(75,38,'pl','błędna atrybucja źródła','błędna atrybucja źródła',1,NULL);

INSERT INTO content_keyword_terms VALUES(76,38,'en','source attribution error','source attribution error',1,NULL);

INSERT INTO content_keyword_terms VALUES(77,39,'pl','bodźce','bodźce',1,NULL);

INSERT INTO content_keyword_terms VALUES(78,39,'en','stimuli','stimuli',1,NULL);

INSERT INTO content_keyword_terms VALUES(79,40,'pl','Boltzmann','boltzmann',1,NULL);

INSERT INTO content_keyword_terms VALUES(80,40,'en','Boltzmann','boltzmann',1,NULL);

INSERT INTO content_keyword_terms VALUES(81,41,'pl','bootstrap','bootstrap',1,NULL);

INSERT INTO content_keyword_terms VALUES(82,41,'en','bootstrap','bootstrap',1,NULL);

INSERT INTO content_keyword_terms VALUES(83,42,'pl','ból','ból',1,NULL);

INSERT INTO content_keyword_terms VALUES(84,42,'en','pain','pain',1,NULL);

INSERT INTO content_keyword_terms VALUES(85,43,'pl','CBT','cbt',1,NULL);

INSERT INTO content_keyword_terms VALUES(86,43,'en','cognitive behavioral therapy','cognitive behavioral therapy',1,NULL);

INSERT INTO content_keyword_terms VALUES(87,44,'pl','Chapman','chapman',1,NULL);

INSERT INTO content_keyword_terms VALUES(88,44,'en','Chapman','chapman',1,NULL);

INSERT INTO content_keyword_terms VALUES(89,45,'pl','chroniczne zmęczenie','chroniczne zmęczenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(90,45,'en','chronic fatigue','chronic fatigue',1,NULL);

INSERT INTO content_keyword_terms VALUES(91,46,'pl','ciągłość','ciągłość',1,NULL);

INSERT INTO content_keyword_terms VALUES(92,46,'en','continuity','continuity',1,NULL);

INSERT INTO content_keyword_terms VALUES(93,47,'pl','codzienność','codzienność',1,NULL);

INSERT INTO content_keyword_terms VALUES(94,47,'en','daily life','daily life',1,NULL);

INSERT INTO content_keyword_terms VALUES(95,48,'pl','cykle','cykle',1,NULL);

INSERT INTO content_keyword_terms VALUES(96,48,'en','cycles','cycles',1,NULL);

INSERT INTO content_keyword_terms VALUES(97,49,'pl','cykliczne zainteresowania','cykliczne zainteresowania',1,NULL);

INSERT INTO content_keyword_terms VALUES(98,49,'en','cyclical interests','cyclical interests',1,NULL);

INSERT INTO content_keyword_terms VALUES(99,50,'pl','cykliczność','cykliczność',1,NULL);

INSERT INTO content_keyword_terms VALUES(100,50,'en','cyclicity','cyclicity',1,NULL);

INSERT INTO content_keyword_terms VALUES(101,51,'pl','czasoprzestrzeń','czasoprzestrzeń',1,NULL);

INSERT INTO content_keyword_terms VALUES(102,51,'en','spacetime','spacetime',1,NULL);

INSERT INTO content_keyword_terms VALUES(103,52,'pl','częstość występowania','częstość występowania',1,NULL);

INSERT INTO content_keyword_terms VALUES(104,52,'en','prevalence','prevalence',1,NULL);

INSERT INTO content_keyword_terms VALUES(105,53,'pl','człowiek w pętli','człowiek w pętli',1,NULL);

INSERT INTO content_keyword_terms VALUES(106,53,'en','human-in-the-loop','human-in-the-loop',1,NULL);

INSERT INTO content_keyword_terms VALUES(107,54,'pl','czynniki rokownicze','czynniki rokownicze',1,NULL);

INSERT INTO content_keyword_terms VALUES(108,54,'en','prognostic factors','prognostic factors',1,NULL);

INSERT INTO content_keyword_terms VALUES(109,55,'pl','dane administracyjne','dane administracyjne',1,NULL);

INSERT INTO content_keyword_terms VALUES(110,55,'en','administrative data','administrative data',1,NULL);

INSERT INTO content_keyword_terms VALUES(111,56,'pl','dane populacyjne','dane populacyjne',1,NULL);

INSERT INTO content_keyword_terms VALUES(112,56,'en','population data','population data',1,NULL);

INSERT INTO content_keyword_terms VALUES(113,57,'pl','dane systemowe','dane systemowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(114,57,'en','system data','system data',1,NULL);

INSERT INTO content_keyword_terms VALUES(115,58,'pl','decyzje techniczne','decyzje techniczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(116,58,'en','technical decision-making','technical decision-making',1,NULL);

INSERT INTO content_keyword_terms VALUES(117,59,'pl','definicja operacyjna','definicja operacyjna',1,NULL);

INSERT INTO content_keyword_terms VALUES(118,59,'en','operational definition','operational definition',1,NULL);

INSERT INTO content_keyword_terms VALUES(119,60,'pl','degradacja informacji','degradacja informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(120,60,'en','information degradation','information degradation',1,NULL);

INSERT INTO content_keyword_terms VALUES(121,61,'pl','dekodowanie społeczne','dekodowanie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(122,61,'en','social decoding','social decoding',1,NULL);

INSERT INTO content_keyword_terms VALUES(123,62,'pl','demografia','demografia',1,NULL);

INSERT INTO content_keyword_terms VALUES(124,62,'en','demographics','demographics',1,NULL);

INSERT INTO content_keyword_terms VALUES(125,63,'pl','depresja','depresja',1,NULL);

INSERT INTO content_keyword_terms VALUES(126,63,'en','depression','depression',1,NULL);

INSERT INTO content_keyword_terms VALUES(127,64,'pl','diagnostyka','diagnostyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(128,64,'en','diagnostic assessment','diagnostic assessment',1,NULL);

INSERT INTO content_keyword_terms VALUES(129,65,'pl','diagnostyka dorosłych','diagnostyka dorosłych',1,NULL);

INSERT INTO content_keyword_terms VALUES(130,65,'en','adult diagnostic assessment','adult diagnostic assessment',1,NULL);

INSERT INTO content_keyword_terms VALUES(131,66,'pl','diagnostyka różnicowa','diagnostyka różnicowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(132,66,'en','differential diagnosis','differential diagnosis',1,NULL);

INSERT INTO content_keyword_terms VALUES(133,67,'pl','diagnoza','diagnoza',1,NULL);

INSERT INTO content_keyword_terms VALUES(134,67,'en','diagnosis','diagnosis',1,NULL);

INSERT INTO content_keyword_terms VALUES(135,68,'pl','diagnozy systemowe','diagnozy systemowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(136,68,'en','system-level diagnosis','system-level diagnosis',1,NULL);

INSERT INTO content_keyword_terms VALUES(137,69,'pl','długie rozmowy','długie rozmowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(138,69,'en','extended conversations','extended conversations',1,NULL);

INSERT INTO content_keyword_terms VALUES(139,70,'pl','dobór próby','dobór próby',1,NULL);

INSERT INTO content_keyword_terms VALUES(140,70,'en','sampling','sampling',1,NULL);

INSERT INTO content_keyword_terms VALUES(141,71,'pl','Donald Knuth','donald knuth',1,NULL);

INSERT INTO content_keyword_terms VALUES(142,71,'en','Donald Knuth','donald knuth',1,NULL);

INSERT INTO content_keyword_terms VALUES(143,72,'pl','dopamina','dopamina',1,NULL);

INSERT INTO content_keyword_terms VALUES(144,72,'en','dopamine','dopamine',1,NULL);

INSERT INTO content_keyword_terms VALUES(145,73,'pl','dopasowanie środowiska','dopasowanie środowiska',1,NULL);

INSERT INTO content_keyword_terms VALUES(146,73,'en','person–environment fit','person–environment fit',1,NULL);

INSERT INTO content_keyword_terms VALUES(147,74,'pl','dopasowanie terapii','dopasowanie terapii',1,NULL);

INSERT INTO content_keyword_terms VALUES(148,74,'en','treatment matching','treatment matching',1,NULL);

INSERT INTO content_keyword_terms VALUES(149,75,'pl','dorosłość','dorosłość',1,NULL);

INSERT INTO content_keyword_terms VALUES(150,75,'en','adulthood','adulthood',1,NULL);

INSERT INTO content_keyword_terms VALUES(151,76,'pl','dosłowność','dosłowność',1,NULL);

INSERT INTO content_keyword_terms VALUES(152,76,'en','literal interpretation','literal interpretation',1,NULL);

INSERT INTO content_keyword_terms VALUES(153,77,'pl','dostępność specjalistów','dostępność specjalistów',1,NULL);

INSERT INTO content_keyword_terms VALUES(154,77,'en','access to specialists','access to specialists',1,NULL);

INSERT INTO content_keyword_terms VALUES(155,78,'pl','doświadczenie wewnętrzne','doświadczenie wewnętrzne',1,NULL);

INSERT INTO content_keyword_terms VALUES(156,78,'en','internal experience','internal experience',1,NULL);

INSERT INTO content_keyword_terms VALUES(157,79,'pl','dotyk','dotyk',1,NULL);

INSERT INTO content_keyword_terms VALUES(158,79,'en','touch','touch',1,NULL);

INSERT INTO content_keyword_terms VALUES(159,80,'pl','drobne znaleziska','drobne znaleziska',1,NULL);

INSERT INTO content_keyword_terms VALUES(160,80,'en','minor findings','minor findings',1,NULL);

INSERT INTO content_keyword_terms VALUES(161,81,'pl','druga zasada termodynamiki','druga zasada termodynamiki',1,NULL);

INSERT INTO content_keyword_terms VALUES(162,81,'en','second law of thermodynamics','second law of thermodynamics',1,NULL);

INSERT INTO content_keyword_terms VALUES(163,82,'pl','duże zbiory danych','duże zbiory danych',1,NULL);

INSERT INTO content_keyword_terms VALUES(164,82,'en','big data','big data',1,NULL);

INSERT INTO content_keyword_terms VALUES(165,83,'pl','dyfuzja tożsamości','dyfuzja tożsamości',1,NULL);

INSERT INTO content_keyword_terms VALUES(166,83,'en','identity diffusion','identity diffusion',1,NULL);

INSERT INTO content_keyword_terms VALUES(167,84,'pl','dyskontowanie nagrody','dyskontowanie nagrody',1,NULL);

INSERT INTO content_keyword_terms VALUES(168,84,'en','reward discounting','reward discounting',1,NULL);

INSERT INTO content_keyword_terms VALUES(169,85,'pl','dysregulacja emocjonalna','dysregulacja emocjonalna',1,NULL);

INSERT INTO content_keyword_terms VALUES(170,85,'en','emotion dysregulation','emotion dysregulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(171,86,'pl','dysregulacja jedzenia','dysregulacja jedzenia',1,NULL);

INSERT INTO content_keyword_terms VALUES(172,86,'en','dysregulated eating','dysregulated eating',1,NULL);

INSERT INTO content_keyword_terms VALUES(173,87,'pl','efekt ironiczny','efekt ironiczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(174,87,'en','ironic process effect','ironic process effect',1,NULL);

INSERT INTO content_keyword_terms VALUES(175,88,'pl','ekspozycja','ekspozycja',1,NULL);

INSERT INTO content_keyword_terms VALUES(176,88,'en','exposure','exposure',1,NULL);

INSERT INTO content_keyword_terms VALUES(177,89,'pl','elastyczność','elastyczność',1,NULL);

INSERT INTO content_keyword_terms VALUES(178,89,'en','flexibility','flexibility',1,NULL);

INSERT INTO content_keyword_terms VALUES(179,90,'pl','elektromagnetyzm','elektromagnetyzm',1,NULL);

INSERT INTO content_keyword_terms VALUES(180,90,'en','electromagnetism','electromagnetism',1,NULL);

INSERT INTO content_keyword_terms VALUES(181,91,'pl','emocje','emocje',1,NULL);

INSERT INTO content_keyword_terms VALUES(182,91,'en','emotions','emotions',1,NULL);

INSERT INTO content_keyword_terms VALUES(183,92,'pl','empatia','empatia',1,NULL);

INSERT INTO content_keyword_terms VALUES(184,92,'en','empathy','empathy',1,NULL);

INSERT INTO content_keyword_terms VALUES(185,93,'pl','entropia','entropia',1,NULL);

INSERT INTO content_keyword_terms VALUES(186,93,'en','entropy','entropy',1,NULL);

INSERT INTO content_keyword_terms VALUES(187,94,'pl','epidemiologia','epidemiologia',1,NULL);

INSERT INTO content_keyword_terms VALUES(188,94,'en','epidemiology','epidemiology',1,NULL);

INSERT INTO content_keyword_terms VALUES(189,95,'pl','estymacja','estymacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(190,95,'en','estimation','estimation',1,NULL);

INSERT INTO content_keyword_terms VALUES(191,96,'pl','falsyfikacja','falsyfikacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(192,96,'en','falsification','falsification',1,NULL);

INSERT INTO content_keyword_terms VALUES(193,97,'pl','fałszywy kontekst','fałszywy kontekst',1,NULL);

INSERT INTO content_keyword_terms VALUES(194,97,'en','false context','false context',1,NULL);

INSERT INTO content_keyword_terms VALUES(195,98,'pl','fenotyp','fenotyp',1,NULL);

INSERT INTO content_keyword_terms VALUES(196,98,'en','phenotype','phenotype',1,NULL);

INSERT INTO content_keyword_terms VALUES(197,99,'pl','fenotyp AuDHD','fenotyp audhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(198,99,'en','AuDHD phenotype','audhd phenotype',1,NULL);

INSERT INTO content_keyword_terms VALUES(199,100,'pl','filozofia nauki','filozofia nauki',1,NULL);

INSERT INTO content_keyword_terms VALUES(200,100,'en','philosophy of science','philosophy of science',1,NULL);

INSERT INTO content_keyword_terms VALUES(201,101,'pl','filtrowanie sensoryczne','filtrowanie sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(202,101,'en','sensory filtering','sensory filtering',1,NULL);

INSERT INTO content_keyword_terms VALUES(203,102,'pl','fizyka','fizyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(204,102,'en','physics','physics',1,NULL);

INSERT INTO content_keyword_terms VALUES(205,103,'pl','formy różniczkowe','formy różniczkowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(206,103,'en','differential forms','differential forms',1,NULL);

INSERT INTO content_keyword_terms VALUES(207,104,'pl','framing','framing',1,NULL);

INSERT INTO content_keyword_terms VALUES(208,104,'en','framing','framing',1,NULL);

INSERT INTO content_keyword_terms VALUES(209,105,'pl','fundamenty IT','fundamenty it',1,NULL);

INSERT INTO content_keyword_terms VALUES(210,105,'en','foundations of information technology','foundations of information technology',1,NULL);

INSERT INTO content_keyword_terms VALUES(211,106,'pl','fundatorzy IT','fundatorzy it',1,NULL);

INSERT INTO content_keyword_terms VALUES(212,106,'en','founders of information technology','founders of information technology',1,NULL);

INSERT INTO content_keyword_terms VALUES(213,107,'pl','funkcje wykonawcze','funkcje wykonawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(214,107,'en','executive function','executive function',1,NULL);

INSERT INTO content_keyword_terms VALUES(215,108,'pl','funkcjonowanie pod presją','funkcjonowanie pod presją',1,NULL);

INSERT INTO content_keyword_terms VALUES(216,108,'en','performance under pressure','performance under pressure',1,NULL);

INSERT INTO content_keyword_terms VALUES(217,109,'pl','genetyka','genetyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(218,109,'en','genetics','genetics',1,NULL);

INSERT INTO content_keyword_terms VALUES(219,110,'pl','geometria','geometria',1,NULL);

INSERT INTO content_keyword_terms VALUES(220,110,'en','geometry','geometry',1,NULL);

INSERT INTO content_keyword_terms VALUES(221,111,'pl','gist','gist',1,NULL);

INSERT INTO content_keyword_terms VALUES(222,111,'en','gist','gist',1,NULL);

INSERT INTO content_keyword_terms VALUES(223,112,'pl','głęboki nacisk','głęboki nacisk',1,NULL);

INSERT INTO content_keyword_terms VALUES(224,112,'en','deep pressure','deep pressure',1,NULL);

INSERT INTO content_keyword_terms VALUES(225,113,'pl','głos pacjentów','głos pacjentów',1,NULL);

INSERT INTO content_keyword_terms VALUES(226,113,'en','patient perspectives','patient perspectives',1,NULL);

INSERT INTO content_keyword_terms VALUES(227,114,'pl','głód','głód',1,NULL);

INSERT INTO content_keyword_terms VALUES(228,114,'en','hunger','hunger',1,NULL);

INSERT INTO content_keyword_terms VALUES(229,115,'pl','głód bliskości','głód bliskości',1,NULL);

INSERT INTO content_keyword_terms VALUES(230,115,'en','need for intimacy','need for intimacy',1,NULL);

INSERT INTO content_keyword_terms VALUES(231,116,'pl','GNU','gnu',1,NULL);

INSERT INTO content_keyword_terms VALUES(232,116,'en','GNU','gnu',1,NULL);

INSERT INTO content_keyword_terms VALUES(233,117,'pl','graf zależności','graf zależności',1,NULL);

INSERT INTO content_keyword_terms VALUES(234,117,'en','dependency graph','dependency graph',1,NULL);

INSERT INTO content_keyword_terms VALUES(235,118,'pl','granica Landauera','granica landauera',1,NULL);

INSERT INTO content_keyword_terms VALUES(236,118,'en','Landauer limit','landauer limit',1,NULL);

INSERT INTO content_keyword_terms VALUES(237,119,'pl','granica Tsirelsona','granica tsirelsona',1,NULL);

INSERT INTO content_keyword_terms VALUES(238,119,'en','Tsirelson bound','tsirelson bound',1,NULL);

INSERT INTO content_keyword_terms VALUES(239,120,'pl','granice','granice',1,NULL);

INSERT INTO content_keyword_terms VALUES(240,120,'en','boundaries','boundaries',1,NULL);

INSERT INTO content_keyword_terms VALUES(241,121,'pl','grawitacja','grawitacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(242,121,'en','gravity','gravity',1,NULL);

INSERT INTO content_keyword_terms VALUES(243,122,'pl','grawitacja kwantowa','grawitacja kwantowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(244,122,'en','quantum gravity','quantum gravity',1,NULL);

INSERT INTO content_keyword_terms VALUES(245,123,'pl','gra słów','gra słów',1,NULL);

INSERT INTO content_keyword_terms VALUES(246,123,'en','wordplay','wordplay',1,NULL);

INSERT INTO content_keyword_terms VALUES(247,124,'pl','gromadzenie informacji','gromadzenie informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(248,124,'en','information accumulation','information accumulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(249,125,'pl','GUS','gus',1,NULL);

INSERT INTO content_keyword_terms VALUES(250,125,'en','Statistics Poland','statistics poland',1,NULL);

INSERT INTO content_keyword_terms VALUES(251,126,'pl','habituacja','habituacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(252,126,'en','habituation','habituation',1,NULL);

INSERT INTO content_keyword_terms VALUES(253,127,'pl','Hadoop','hadoop',1,NULL);

INSERT INTO content_keyword_terms VALUES(254,127,'en','Hadoop','hadoop',1,NULL);

INSERT INTO content_keyword_terms VALUES(255,128,'pl','HALT','halt',1,NULL);

INSERT INTO content_keyword_terms VALUES(256,128,'en','HALT','halt',1,NULL);

INSERT INTO content_keyword_terms VALUES(257,129,'pl','hamowanie reakcji','hamowanie reakcji',1,NULL);

INSERT INTO content_keyword_terms VALUES(258,129,'en','response inhibition','response inhibition',1,NULL);

INSERT INTO content_keyword_terms VALUES(259,130,'pl','hiperfokus','hiperfokus',1,NULL);

INSERT INTO content_keyword_terms VALUES(260,130,'en','hyperfocus','hyperfocus',1,NULL);

INSERT INTO content_keyword_terms VALUES(261,131,'pl','hipokamp','hipokamp',1,NULL);

INSERT INTO content_keyword_terms VALUES(262,131,'en','hippocampus','hippocampus',1,NULL);

INSERT INTO content_keyword_terms VALUES(263,132,'pl','hipoteza','hipoteza',1,NULL);

INSERT INTO content_keyword_terms VALUES(264,132,'en','hypothesis','hypothesis',1,NULL);

INSERT INTO content_keyword_terms VALUES(265,133,'pl','historia diagnostyki','historia diagnostyki',1,NULL);

INSERT INTO content_keyword_terms VALUES(266,133,'en','diagnostic history','diagnostic history',1,NULL);

INSERT INTO content_keyword_terms VALUES(267,134,'pl','historia informatyki','historia informatyki',1,NULL);

INSERT INTO content_keyword_terms VALUES(268,134,'en','history of computing','history of computing',1,NULL);

INSERT INTO content_keyword_terms VALUES(269,135,'pl','historia medyczna','historia medyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(270,135,'en','medical history','medical history',1,NULL);

INSERT INTO content_keyword_terms VALUES(271,136,'pl','historia rozmowy','historia rozmowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(272,136,'en','conversation history','conversation history',1,NULL);

INSERT INTO content_keyword_terms VALUES(273,137,'pl','humor','humor',1,NULL);

INSERT INTO content_keyword_terms VALUES(274,137,'en','humor','humor',1,NULL);

INSERT INTO content_keyword_terms VALUES(275,138,'pl','identyfikacja','identyfikacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(276,138,'en','identification','identification',1,NULL);

INSERT INTO content_keyword_terms VALUES(277,139,'pl','impulsywność','impulsywność',1,NULL);

INSERT INTO content_keyword_terms VALUES(278,139,'en','impulsivity','impulsivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(279,140,'pl','impulsywność społeczna','impulsywność społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(280,140,'en','social impulsivity','social impulsivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(281,141,'pl','inercja autystyczna','inercja autystyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(282,141,'en','autistic inertia','autistic inertia',1,NULL);

INSERT INTO content_keyword_terms VALUES(283,142,'pl','infodumping','infodumping',1,NULL);

INSERT INTO content_keyword_terms VALUES(284,142,'en','infodumping','infodumping',1,NULL);

INSERT INTO content_keyword_terms VALUES(285,143,'pl','infodumping jako język miłości','infodumping jako język miłości',1,NULL);

INSERT INTO content_keyword_terms VALUES(286,143,'en','infodumping as a love language','infodumping as a love language',1,NULL);

INSERT INTO content_keyword_terms VALUES(287,144,'pl','informatyka','informatyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(288,144,'en','computer science','computer science',1,NULL);

INSERT INTO content_keyword_terms VALUES(289,145,'pl','inicjowanie zadań','inicjowanie zadań',1,NULL);

INSERT INTO content_keyword_terms VALUES(290,145,'en','task initiation','task initiation',1,NULL);

INSERT INTO content_keyword_terms VALUES(291,146,'pl','inkubacja','inkubacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(292,146,'en','incubation','incubation',1,NULL);

INSERT INTO content_keyword_terms VALUES(293,147,'pl','instrukcje pozytywne','instrukcje pozytywne',1,NULL);

INSERT INTO content_keyword_terms VALUES(294,147,'en','positive instructions','positive instructions',1,NULL);

INSERT INTO content_keyword_terms VALUES(295,148,'pl','intelektualizacja','intelektualizacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(296,148,'en','intellectualization','intellectualization',1,NULL);

INSERT INTO content_keyword_terms VALUES(297,149,'pl','intensywna empatia','intensywna empatia',1,NULL);

INSERT INTO content_keyword_terms VALUES(298,149,'en','heightened empathy','heightened empathy',1,NULL);

INSERT INTO content_keyword_terms VALUES(299,150,'pl','intensywność','intensywność',1,NULL);

INSERT INTO content_keyword_terms VALUES(300,150,'en','intensity','intensity',1,NULL);

INSERT INTO content_keyword_terms VALUES(301,151,'pl','interocepcja','interocepcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(302,151,'en','interoception','interoception',1,NULL);

INSERT INTO content_keyword_terms VALUES(303,152,'pl','interpretacja kliniczna','interpretacja kliniczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(304,152,'en','clinical interpretation','clinical interpretation',1,NULL);

INSERT INTO content_keyword_terms VALUES(305,153,'pl','JavaScript','javascript',1,NULL);

INSERT INTO content_keyword_terms VALUES(306,153,'en','JavaScript','javascript',1,NULL);

INSERT INTO content_keyword_terms VALUES(307,154,'pl','jedzenie','jedzenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(308,154,'en','eating','eating',1,NULL);

INSERT INTO content_keyword_terms VALUES(309,155,'pl','języki miłości','języki miłości',1,NULL);

INSERT INTO content_keyword_terms VALUES(310,155,'en','love languages','love languages',1,NULL);

INSERT INTO content_keyword_terms VALUES(311,156,'pl','języki programowania','języki programowania',1,NULL);

INSERT INTO content_keyword_terms VALUES(312,156,'en','programming languages','programming languages',1,NULL);

INSERT INTO content_keyword_terms VALUES(313,157,'pl','język C','język c',1,NULL);

INSERT INTO content_keyword_terms VALUES(314,157,'en','C programming language','c programming language',1,NULL);

INSERT INTO content_keyword_terms VALUES(315,158,'pl','kameleonizm','kameleonizm',1,NULL);

INSERT INTO content_keyword_terms VALUES(316,158,'en','social chameleonism','social chameleonism',1,NULL);

INSERT INTO content_keyword_terms VALUES(317,159,'pl','Ken Thompson','ken thompson',1,NULL);

INSERT INTO content_keyword_terms VALUES(318,159,'en','Ken Thompson','ken thompson',1,NULL);

INSERT INTO content_keyword_terms VALUES(319,160,'pl','klasyfikacja diagnostyczna','klasyfikacja diagnostyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(320,160,'en','diagnostic classification','diagnostic classification',1,NULL);

INSERT INTO content_keyword_terms VALUES(321,161,'pl','kod źródłowy','kod źródłowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(322,161,'en','source code','source code',1,NULL);

INSERT INTO content_keyword_terms VALUES(323,162,'pl','kognitywistyka','kognitywistyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(324,162,'en','cognitive science','cognitive science',1,NULL);

INSERT INTO content_keyword_terms VALUES(325,163,'pl','kohorta','kohorta',1,NULL);

INSERT INTO content_keyword_terms VALUES(326,163,'en','cohort','cohort',1,NULL);

INSERT INTO content_keyword_terms VALUES(327,164,'pl','kolejność zadań','kolejność zadań',1,NULL);

INSERT INTO content_keyword_terms VALUES(328,164,'en','task sequencing','task sequencing',1,NULL);

INSERT INTO content_keyword_terms VALUES(329,165,'pl','komisja konkursowa','komisja konkursowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(330,165,'en','selection committee','selection committee',1,NULL);

INSERT INTO content_keyword_terms VALUES(331,166,'pl','kompensacja','kompensacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(332,166,'en','compensation','compensation',1,NULL);

INSERT INTO content_keyword_terms VALUES(333,167,'pl','kompensacja autyzm–ADHD','kompensacja autyzm–adhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(334,167,'en','autism–ADHD compensation','autism–adhd compensation',1,NULL);

INSERT INTO content_keyword_terms VALUES(335,168,'pl','kompetencje','kompetencje',1,NULL);

INSERT INTO content_keyword_terms VALUES(336,168,'en','competencies','competencies',1,NULL);

INSERT INTO content_keyword_terms VALUES(337,169,'pl','kompetencje terapeuty','kompetencje terapeuty',1,NULL);

INSERT INTO content_keyword_terms VALUES(338,169,'en','therapist competence','therapist competence',1,NULL);

INSERT INTO content_keyword_terms VALUES(339,170,'pl','kompilatory','kompilatory',1,NULL);

INSERT INTO content_keyword_terms VALUES(340,170,'en','compilers','compilers',1,NULL);

INSERT INTO content_keyword_terms VALUES(341,171,'pl','kompresja','kompresja',1,NULL);

INSERT INTO content_keyword_terms VALUES(342,171,'en','compression','compression',1,NULL);

INSERT INTO content_keyword_terms VALUES(343,172,'pl','kompresja stratna','kompresja stratna',1,NULL);

INSERT INTO content_keyword_terms VALUES(344,172,'en','lossy compression','lossy compression',1,NULL);

INSERT INTO content_keyword_terms VALUES(345,173,'pl','kompromis poznawczy','kompromis poznawczy',1,NULL);

INSERT INTO content_keyword_terms VALUES(346,173,'en','cognitive trade-off','cognitive trade-off',1,NULL);

INSERT INTO content_keyword_terms VALUES(347,174,'pl','komputery osobiste','komputery osobiste',1,NULL);

INSERT INTO content_keyword_terms VALUES(348,174,'en','personal computers','personal computers',1,NULL);

INSERT INTO content_keyword_terms VALUES(349,175,'pl','komunikacja','komunikacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(350,175,'en','communication','communication',1,NULL);

INSERT INTO content_keyword_terms VALUES(351,176,'pl','komunikacja niewerbalna','komunikacja niewerbalna',1,NULL);

INSERT INTO content_keyword_terms VALUES(352,176,'en','nonverbal communication','nonverbal communication',1,NULL);

INSERT INTO content_keyword_terms VALUES(353,177,'pl','komunikacja społeczna','komunikacja społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(354,177,'en','social communication','social communication',1,NULL);

INSERT INTO content_keyword_terms VALUES(355,178,'pl','konfabulacja','konfabulacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(356,178,'en','confabulation','confabulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(357,179,'pl','konflikt interesów','konflikt interesów',1,NULL);

INSERT INTO content_keyword_terms VALUES(358,179,'en','conflict of interest','conflict of interest',1,NULL);

INSERT INTO content_keyword_terms VALUES(359,180,'pl','konflikt potrzeb','konflikt potrzeb',1,NULL);

INSERT INTO content_keyword_terms VALUES(360,180,'en','needs conflict','needs conflict',1,NULL);

INSERT INTO content_keyword_terms VALUES(361,181,'pl','konflikt relacyjny','konflikt relacyjny',1,NULL);

INSERT INTO content_keyword_terms VALUES(362,181,'en','relational conflict','relational conflict',1,NULL);

INSERT INTO content_keyword_terms VALUES(363,182,'pl','konflikt rutyna–nowość','konflikt rutyna–nowość',1,NULL);

INSERT INTO content_keyword_terms VALUES(364,182,'en','routine–novelty conflict','routine–novelty conflict',1,NULL);

INSERT INTO content_keyword_terms VALUES(365,183,'pl','konflikt wewnętrzny','konflikt wewnętrzny',1,NULL);

INSERT INTO content_keyword_terms VALUES(366,183,'en','internal conflict','internal conflict',1,NULL);

INSERT INTO content_keyword_terms VALUES(367,184,'pl','konieczność','konieczność',1,NULL);

INSERT INTO content_keyword_terms VALUES(368,184,'en','necessity','necessity',1,NULL);

INSERT INTO content_keyword_terms VALUES(369,185,'pl','konsolidacja pamięci','konsolidacja pamięci',1,NULL);

INSERT INTO content_keyword_terms VALUES(370,185,'en','memory consolidation','memory consolidation',1,NULL);

INSERT INTO content_keyword_terms VALUES(371,186,'pl','kontakt społeczny','kontakt społeczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(372,186,'en','social contact','social contact',1,NULL);

INSERT INTO content_keyword_terms VALUES(373,187,'pl','kontekstowość','kontekstowość',1,NULL);

INSERT INTO content_keyword_terms VALUES(374,187,'en','context dependence','context dependence',1,NULL);

INSERT INTO content_keyword_terms VALUES(375,188,'pl','kontekst rozmowy','kontekst rozmowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(376,188,'en','conversational context','conversational context',1,NULL);

INSERT INTO content_keyword_terms VALUES(377,189,'pl','kontrola wykonawcza','kontrola wykonawcza',1,NULL);

INSERT INTO content_keyword_terms VALUES(378,189,'en','executive control','executive control',1,NULL);

INSERT INTO content_keyword_terms VALUES(379,190,'pl','kontrprzykład','kontrprzykład',1,NULL);

INSERT INTO content_keyword_terms VALUES(380,190,'en','counterexample','counterexample',1,NULL);

INSERT INTO content_keyword_terms VALUES(381,191,'pl','koordynacja ruchowa','koordynacja ruchowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(382,191,'en','motor coordination','motor coordination',1,NULL);

INSERT INTO content_keyword_terms VALUES(383,192,'pl','kora mózgowa','kora mózgowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(384,192,'en','cerebral cortex','cerebral cortex',1,NULL);

INSERT INTO content_keyword_terms VALUES(385,193,'pl','korekta błędu','korekta błędu',1,NULL);

INSERT INTO content_keyword_terms VALUES(386,193,'en','error correction','error correction',1,NULL);

INSERT INTO content_keyword_terms VALUES(387,194,'pl','korekta zewnętrzna','korekta zewnętrzna',1,NULL);

INSERT INTO content_keyword_terms VALUES(388,194,'en','external correction','external correction',1,NULL);

INSERT INTO content_keyword_terms VALUES(389,195,'pl','korelacja','korelacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(390,195,'en','correlation','correlation',1,NULL);

INSERT INTO content_keyword_terms VALUES(391,196,'pl','kosmologia kwantowa','kosmologia kwantowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(392,196,'en','quantum cosmology','quantum cosmology',1,NULL);

INSERT INTO content_keyword_terms VALUES(393,197,'pl','koszt poznawczy','koszt poznawczy',1,NULL);

INSERT INTO content_keyword_terms VALUES(394,197,'en','cognitive cost','cognitive cost',1,NULL);

INSERT INTO content_keyword_terms VALUES(395,198,'pl','kreatywność','kreatywność',1,NULL);

INSERT INTO content_keyword_terms VALUES(396,198,'en','creativity','creativity',1,NULL);

INSERT INTO content_keyword_terms VALUES(397,199,'pl','kryzys tożsamości','kryzys tożsamości',1,NULL);

INSERT INTO content_keyword_terms VALUES(398,199,'en','identity crisis','identity crisis',1,NULL);

INSERT INTO content_keyword_terms VALUES(399,200,'pl','leczenie ADHD','leczenie adhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(400,200,'en','ADHD treatment','adhd treatment',1,NULL);

INSERT INTO content_keyword_terms VALUES(401,201,'pl','leki','leki',1,NULL);

INSERT INTO content_keyword_terms VALUES(402,201,'en','medications','medications',1,NULL);

INSERT INTO content_keyword_terms VALUES(403,202,'pl','lęk','lęk',1,NULL);

INSERT INTO content_keyword_terms VALUES(404,202,'en','anxiety','anxiety',1,NULL);

INSERT INTO content_keyword_terms VALUES(405,203,'pl','lęk kompensacyjny','lęk kompensacyjny',1,NULL);

INSERT INTO content_keyword_terms VALUES(406,203,'en','compensatory anxiety','compensatory anxiety',1,NULL);

INSERT INTO content_keyword_terms VALUES(407,204,'pl','lęk przed błędem','lęk przed błędem',1,NULL);

INSERT INTO content_keyword_terms VALUES(408,204,'en','fear of error','fear of error',1,NULL);

INSERT INTO content_keyword_terms VALUES(409,205,'pl','lęk relacyjny','lęk relacyjny',1,NULL);

INSERT INTO content_keyword_terms VALUES(410,205,'en','relationship anxiety','relationship anxiety',1,NULL);

INSERT INTO content_keyword_terms VALUES(411,206,'pl','lęk społeczny','lęk społeczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(412,206,'en','social anxiety','social anxiety',1,NULL);

INSERT INTO content_keyword_terms VALUES(413,207,'pl','liczba dorosłych','liczba dorosłych',1,NULL);

INSERT INTO content_keyword_terms VALUES(414,207,'en','number of adults','number of adults',1,NULL);

INSERT INTO content_keyword_terms VALUES(415,208,'pl','liczba osób','liczba osób',1,NULL);

INSERT INTO content_keyword_terms VALUES(416,208,'en','number of individuals','number of individuals',1,NULL);

INSERT INTO content_keyword_terms VALUES(417,209,'pl','limit czasu','limit czasu',1,NULL);

INSERT INTO content_keyword_terms VALUES(418,209,'en','time limit','time limit',1,NULL);

INSERT INTO content_keyword_terms VALUES(419,210,'pl','Linus Torvalds','linus torvalds',1,NULL);

INSERT INTO content_keyword_terms VALUES(420,210,'en','Linus Torvalds','linus torvalds',1,NULL);

INSERT INTO content_keyword_terms VALUES(421,211,'pl','Linux','linux',1,NULL);

INSERT INTO content_keyword_terms VALUES(422,211,'en','Linux','linux',1,NULL);

INSERT INTO content_keyword_terms VALUES(423,212,'pl','małomówność','małomówność',1,NULL);

INSERT INTO content_keyword_terms VALUES(424,212,'en','reduced verbal output','reduced verbal output',1,NULL);

INSERT INTO content_keyword_terms VALUES(425,213,'pl','MapReduce','mapreduce',1,NULL);

INSERT INTO content_keyword_terms VALUES(426,213,'en','MapReduce','mapreduce',1,NULL);

INSERT INTO content_keyword_terms VALUES(427,214,'pl','maskowanie','maskowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(428,214,'en','camouflaging','camouflaging',1,NULL);

INSERT INTO content_keyword_terms VALUES(429,215,'pl','maskowanie i impulsywność społeczna','maskowanie i impulsywność społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(430,215,'en','camouflaging and social impulsivity','camouflaging and social impulsivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(431,216,'pl','mechanika klasyczna','mechanika klasyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(432,216,'en','classical mechanics','classical mechanics',1,NULL);

INSERT INTO content_keyword_terms VALUES(433,217,'pl','mechanika kwantowa','mechanika kwantowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(434,217,'en','quantum mechanics','quantum mechanics',1,NULL);

INSERT INTO content_keyword_terms VALUES(435,218,'pl','mechanika płynów','mechanika płynów',1,NULL);

INSERT INTO content_keyword_terms VALUES(436,218,'en','fluid mechanics','fluid mechanics',1,NULL);

INSERT INTO content_keyword_terms VALUES(437,219,'pl','mechanizmy obronne','mechanizmy obronne',1,NULL);

INSERT INTO content_keyword_terms VALUES(438,219,'en','defense mechanisms','defense mechanisms',1,NULL);

INSERT INTO content_keyword_terms VALUES(439,220,'pl','mechanizmy społeczne','mechanizmy społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(440,220,'en','social mechanisms','social mechanisms',1,NULL);

INSERT INTO content_keyword_terms VALUES(441,221,'pl','Memento','memento',1,NULL);

INSERT INTO content_keyword_terms VALUES(442,221,'en','Memento','memento',1,NULL);

INSERT INTO content_keyword_terms VALUES(443,222,'pl','metadane','metadane',1,NULL);

INSERT INTO content_keyword_terms VALUES(444,222,'en','metadata','metadata',1,NULL);

INSERT INTO content_keyword_terms VALUES(445,223,'pl','metafizyka','metafizyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(446,223,'en','metaphysics','metaphysics',1,NULL);

INSERT INTO content_keyword_terms VALUES(447,224,'pl','metafora','metafora',1,NULL);

INSERT INTO content_keyword_terms VALUES(448,224,'en','metaphor','metaphor',1,NULL);

INSERT INTO content_keyword_terms VALUES(449,225,'pl','metapoziom','metapoziom',1,NULL);

INSERT INTO content_keyword_terms VALUES(450,225,'en','meta-level','meta-level',1,NULL);

INSERT INTO content_keyword_terms VALUES(451,226,'pl','metapoznanie','metapoznanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(452,226,'en','metacognition','metacognition',1,NULL);

INSERT INTO content_keyword_terms VALUES(453,227,'pl','metaprogramowanie','metaprogramowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(454,227,'en','metaprogramming','metaprogramming',1,NULL);

INSERT INTO content_keyword_terms VALUES(455,228,'pl','mindfulness','mindfulness',1,NULL);

INSERT INTO content_keyword_terms VALUES(456,228,'en','mindfulness','mindfulness',1,NULL);

INSERT INTO content_keyword_terms VALUES(457,229,'pl','model obliczeniowy','model obliczeniowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(458,229,'en','computational model','computational model',1,NULL);

INSERT INTO content_keyword_terms VALUES(459,230,'pl','model statystyczny','model statystyczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(460,230,'en','statistical model','statistical model',1,NULL);

INSERT INTO content_keyword_terms VALUES(461,231,'pl','model wewnętrzny','model wewnętrzny',1,NULL);

INSERT INTO content_keyword_terms VALUES(462,231,'en','internal model','internal model',1,NULL);

INSERT INTO content_keyword_terms VALUES(463,232,'pl','monolog wewnętrzny','monolog wewnętrzny',1,NULL);

INSERT INTO content_keyword_terms VALUES(464,232,'en','inner speech','inner speech',1,NULL);

INSERT INTO content_keyword_terms VALUES(465,233,'pl','monotropizm','monotropizm',1,NULL);

INSERT INTO content_keyword_terms VALUES(466,233,'en','monotropism','monotropism',1,NULL);

INSERT INTO content_keyword_terms VALUES(467,234,'pl','motywacja','motywacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(468,234,'en','motivation','motivation',1,NULL);

INSERT INTO content_keyword_terms VALUES(469,235,'pl','myślenie dychotomiczne','myślenie dychotomiczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(470,235,'en','dichotomous thinking','dichotomous thinking',1,NULL);

INSERT INTO content_keyword_terms VALUES(471,236,'pl','myślenie oddolne','myślenie oddolne',1,NULL);

INSERT INTO content_keyword_terms VALUES(472,236,'en','bottom-up processing','bottom-up processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(473,237,'pl','myślenie systemowe','myślenie systemowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(474,237,'en','systems thinking','systems thinking',1,NULL);

INSERT INTO content_keyword_terms VALUES(475,238,'pl','nadmierne przepraszanie','nadmierne przepraszanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(476,238,'en','excessive apologizing','excessive apologizing',1,NULL);

INSERT INTO content_keyword_terms VALUES(477,239,'pl','nadwrażliwość','nadwrażliwość',1,NULL);

INSERT INTO content_keyword_terms VALUES(478,239,'en','hypersensitivity','hypersensitivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(479,240,'pl','nagroda natychmiastowa','nagroda natychmiastowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(480,240,'en','immediate reward','immediate reward',1,NULL);

INSERT INTO content_keyword_terms VALUES(481,241,'pl','narracja','narracja',1,NULL);

INSERT INTO content_keyword_terms VALUES(482,241,'en','narrative','narrative',1,NULL);

INSERT INTO content_keyword_terms VALUES(483,242,'pl','natłok myśli','natłok myśli',1,NULL);

INSERT INTO content_keyword_terms VALUES(484,242,'en','racing thoughts','racing thoughts',1,NULL);

INSERT INTO content_keyword_terms VALUES(485,243,'pl','nawigacja systemu','nawigacja systemu',1,NULL);

INSERT INTO content_keyword_terms VALUES(486,243,'en','system navigation','system navigation',1,NULL);

INSERT INTO content_keyword_terms VALUES(487,244,'pl','nawyki','nawyki',1,NULL);

INSERT INTO content_keyword_terms VALUES(488,244,'en','habits','habits',1,NULL);

INSERT INTO content_keyword_terms VALUES(489,245,'pl','nawyki wszystko albo nic','nawyki wszystko albo nic',1,NULL);

INSERT INTO content_keyword_terms VALUES(490,245,'en','all-or-nothing habits','all-or-nothing habits',1,NULL);

INSERT INTO content_keyword_terms VALUES(491,246,'pl','negacja','negacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(492,246,'en','negation','negation',1,NULL);

INSERT INTO content_keyword_terms VALUES(493,247,'pl','neurobiologia','neurobiologia',1,NULL);

INSERT INTO content_keyword_terms VALUES(494,247,'en','neurobiology','neurobiology',1,NULL);

INSERT INTO content_keyword_terms VALUES(495,248,'pl','neurobiologia snu','neurobiologia snu',1,NULL);

INSERT INTO content_keyword_terms VALUES(496,248,'en','sleep neurobiology','sleep neurobiology',1,NULL);

INSERT INTO content_keyword_terms VALUES(497,249,'pl','niedodiagnozowanie','niedodiagnozowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(498,249,'en','underdiagnosis','underdiagnosis',1,NULL);

INSERT INTO content_keyword_terms VALUES(499,250,'pl','niedopasowanie interwencji','niedopasowanie interwencji',1,NULL);

INSERT INTO content_keyword_terms VALUES(500,250,'en','intervention mismatch','intervention mismatch',1,NULL);

INSERT INTO content_keyword_terms VALUES(501,251,'pl','niedowrażliwość','niedowrażliwość',1,NULL);

INSERT INTO content_keyword_terms VALUES(502,251,'en','hyposensitivity','hyposensitivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(503,252,'pl','niejednoznaczność','niejednoznaczność',1,NULL);

INSERT INTO content_keyword_terms VALUES(504,252,'en','ambiguity','ambiguity',1,NULL);

INSERT INTO content_keyword_terms VALUES(505,253,'pl','nieliniowe wykonywanie zadań','nieliniowe wykonywanie zadań',1,NULL);

INSERT INTO content_keyword_terms VALUES(506,253,'en','nonlinear task execution','nonlinear task execution',1,NULL);

INSERT INTO content_keyword_terms VALUES(507,254,'pl','nieliniowość','nieliniowość',1,NULL);

INSERT INTO content_keyword_terms VALUES(508,254,'en','nonlinearity','nonlinearity',1,NULL);

INSERT INTO content_keyword_terms VALUES(509,255,'pl','nielokalność','nielokalność',1,NULL);

INSERT INTO content_keyword_terms VALUES(510,255,'en','nonlocality','nonlocality',1,NULL);

INSERT INTO content_keyword_terms VALUES(511,256,'pl','niepewność','niepewność',1,NULL);

INSERT INTO content_keyword_terms VALUES(512,256,'en','uncertainty','uncertainty',1,NULL);

INSERT INTO content_keyword_terms VALUES(513,257,'pl','niepodważanie diagnozy','niepodważanie diagnozy',1,NULL);

INSERT INTO content_keyword_terms VALUES(514,257,'en','diagnostic acceptance','diagnostic acceptance',1,NULL);

INSERT INTO content_keyword_terms VALUES(515,258,'pl','nieporozumienie','nieporozumienie',1,NULL);

INSERT INTO content_keyword_terms VALUES(516,258,'en','misunderstanding','misunderstanding',1,NULL);

INSERT INTO content_keyword_terms VALUES(517,259,'pl','nierówności Bella','nierówności bella',1,NULL);

INSERT INTO content_keyword_terms VALUES(518,259,'en','Bell inequalities','bell inequalities',1,NULL);

INSERT INTO content_keyword_terms VALUES(519,260,'pl','niesprawiedliwość','niesprawiedliwość',1,NULL);

INSERT INTO content_keyword_terms VALUES(520,260,'en','injustice','injustice',1,NULL);

INSERT INTO content_keyword_terms VALUES(521,261,'pl','nietypowe reakcje na leki','nietypowe reakcje na leki',1,NULL);

INSERT INTO content_keyword_terms VALUES(522,261,'en','atypical drug responses','atypical drug responses',1,NULL);

INSERT INTO content_keyword_terms VALUES(523,262,'pl','niewykorzystany potencjał','niewykorzystany potencjał',1,NULL);

INSERT INTO content_keyword_terms VALUES(524,262,'en','unrealized potential','unrealized potential',1,NULL);

INSERT INTO content_keyword_terms VALUES(525,263,'pl','niezawodność','niezawodność',1,NULL);

INSERT INTO content_keyword_terms VALUES(526,263,'en','reliability','reliability',1,NULL);

INSERT INTO content_keyword_terms VALUES(527,264,'pl','niski koszt tłumaczenia','niski koszt tłumaczenia',1,NULL);

INSERT INTO content_keyword_terms VALUES(528,264,'en','low explanatory cost','low explanatory cost',1,NULL);

INSERT INTO content_keyword_terms VALUES(529,265,'pl','noradrenalina','noradrenalina',1,NULL);

INSERT INTO content_keyword_terms VALUES(530,265,'en','norepinephrine','norepinephrine',1,NULL);

INSERT INTO content_keyword_terms VALUES(531,266,'pl','nostalgia regulacyjna','nostalgia regulacyjna',1,NULL);

INSERT INTO content_keyword_terms VALUES(532,266,'en','regulatory nostalgia','regulatory nostalgia',1,NULL);

INSERT INTO content_keyword_terms VALUES(533,267,'pl','nowe dane','nowe dane',1,NULL);

INSERT INTO content_keyword_terms VALUES(534,267,'en','new data','new data',1,NULL);

INSERT INTO content_keyword_terms VALUES(535,268,'pl','obiektywność','obiektywność',1,NULL);

INSERT INTO content_keyword_terms VALUES(536,268,'en','objectivity','objectivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(537,269,'pl','objawy somatyczne','objawy somatyczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(538,269,'en','somatic symptoms','somatic symptoms',1,NULL);

INSERT INTO content_keyword_terms VALUES(539,270,'pl','objawy wtórne','objawy wtórne',1,NULL);

INSERT INTO content_keyword_terms VALUES(540,270,'en','secondary symptoms','secondary symptoms',1,NULL);

INSERT INTO content_keyword_terms VALUES(541,271,'pl','obserwacja społeczna','obserwacja społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(542,271,'en','social observation','social observation',1,NULL);

INSERT INTO content_keyword_terms VALUES(543,272,'pl','odkrywanie siebie','odkrywanie siebie',1,NULL);

INSERT INTO content_keyword_terms VALUES(544,272,'en','self-discovery','self-discovery',1,NULL);

INSERT INTO content_keyword_terms VALUES(545,273,'pl','odpowiedzialność','odpowiedzialność',1,NULL);

INSERT INTO content_keyword_terms VALUES(546,273,'en','responsibility','responsibility',1,NULL);

INSERT INTO content_keyword_terms VALUES(547,274,'pl','odrzucenie','odrzucenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(548,274,'en','rejection','rejection',1,NULL);

INSERT INTO content_keyword_terms VALUES(549,275,'pl','odśmiecanie pamięci','odśmiecanie pamięci',1,NULL);

INSERT INTO content_keyword_terms VALUES(550,275,'en','memory decluttering','memory decluttering',1,NULL);

INSERT INTO content_keyword_terms VALUES(551,276,'pl','ogólna teoria względności','ogólna teoria względności',1,NULL);

INSERT INTO content_keyword_terms VALUES(552,276,'en','general relativity','general relativity',1,NULL);

INSERT INTO content_keyword_terms VALUES(553,277,'pl','ograniczenia danych','ograniczenia danych',1,NULL);

INSERT INTO content_keyword_terms VALUES(554,277,'en','data limitations','data limitations',1,NULL);

INSERT INTO content_keyword_terms VALUES(555,278,'pl','ograniczenia sprzętowe','ograniczenia sprzętowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(556,278,'en','hardware constraints','hardware constraints',1,NULL);

INSERT INTO content_keyword_terms VALUES(557,279,'pl','ograniczenia systemowe','ograniczenia systemowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(558,279,'en','system constraints','system constraints',1,NULL);

INSERT INTO content_keyword_terms VALUES(559,280,'pl','ograniczona pamięć','ograniczona pamięć',1,NULL);

INSERT INTO content_keyword_terms VALUES(560,280,'en','limited memory','limited memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(561,281,'pl','operator wykonawczy','operator wykonawczy',1,NULL);

INSERT INTO content_keyword_terms VALUES(562,281,'en','executive operator','executive operator',1,NULL);

INSERT INTO content_keyword_terms VALUES(563,282,'pl','opór','opór',1,NULL);

INSERT INTO content_keyword_terms VALUES(564,282,'en','resistance','resistance',1,NULL);

INSERT INTO content_keyword_terms VALUES(565,283,'pl','opóźnione objawy stresu','opóźnione objawy stresu',1,NULL);

INSERT INTO content_keyword_terms VALUES(566,283,'en','delayed stress symptoms','delayed stress symptoms',1,NULL);

INSERT INTO content_keyword_terms VALUES(567,284,'pl','oprogramowanie','oprogramowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(568,284,'en','software','software',1,NULL);

INSERT INTO content_keyword_terms VALUES(569,285,'pl','organizacja wiedzy','organizacja wiedzy',1,NULL);

INSERT INTO content_keyword_terms VALUES(570,285,'en','knowledge organization','knowledge organization',1,NULL);

INSERT INTO content_keyword_terms VALUES(571,286,'pl','osiągnięcia','osiągnięcia',1,NULL);

INSERT INTO content_keyword_terms VALUES(572,286,'en','achievement','achievement',1,NULL);

INSERT INTO content_keyword_terms VALUES(573,287,'pl','otwarte pętle','otwarte pętle',1,NULL);

INSERT INTO content_keyword_terms VALUES(574,287,'en','open loops','open loops',1,NULL);

INSERT INTO content_keyword_terms VALUES(575,288,'pl','pamięć','pamięć',1,NULL);

INSERT INTO content_keyword_terms VALUES(576,288,'en','memory','memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(577,289,'pl','pamięć AI','pamięć ai',1,NULL);

INSERT INTO content_keyword_terms VALUES(578,289,'en','AI memory','ai memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(579,290,'pl','pamięć asocjacyjna','pamięć asocjacyjna',1,NULL);

INSERT INTO content_keyword_terms VALUES(580,290,'en','associative memory','associative memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(581,291,'pl','pamięć autobiograficzna','pamięć autobiograficzna',1,NULL);

INSERT INTO content_keyword_terms VALUES(582,291,'en','autobiographical memory','autobiographical memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(583,292,'pl','pamięć deklaratywna','pamięć deklaratywna',1,NULL);

INSERT INTO content_keyword_terms VALUES(584,292,'en','declarative memory','declarative memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(585,293,'pl','pamięć długotrwała','pamięć długotrwała',1,NULL);

INSERT INTO content_keyword_terms VALUES(586,293,'en','long-term memory','long-term memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(587,294,'pl','pamięć encyklopedyczna','pamięć encyklopedyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(588,294,'en','encyclopedic memory','encyclopedic memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(589,295,'pl','pamięć epizodyczna','pamięć epizodyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(590,295,'en','episodic memory','episodic memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(591,296,'pl','pamięć komputerowa','pamięć komputerowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(592,296,'en','computer memory','computer memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(593,297,'pl','pamięć krótkotrwała','pamięć krótkotrwała',1,NULL);

INSERT INTO content_keyword_terms VALUES(594,297,'en','short-term memory','short-term memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(595,298,'pl','pamięć ludzka','pamięć ludzka',1,NULL);

INSERT INTO content_keyword_terms VALUES(596,298,'en','human memory','human memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(597,299,'pl','pamięć neuroróżnorodna','pamięć neuroróżnorodna',1,NULL);

INSERT INTO content_keyword_terms VALUES(598,299,'en','neurodivergent memory','neurodivergent memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(599,300,'pl','pamięć proceduralna','pamięć proceduralna',1,NULL);

INSERT INTO content_keyword_terms VALUES(600,300,'en','procedural memory','procedural memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(601,301,'pl','pamięć projektu','pamięć projektu',1,NULL);

INSERT INTO content_keyword_terms VALUES(602,301,'en','project memory','project memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(603,302,'pl','pamięć prospektywna','pamięć prospektywna',1,NULL);

INSERT INTO content_keyword_terms VALUES(604,302,'en','prospective memory','prospective memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(605,303,'pl','pamięć robocza','pamięć robocza',1,NULL);

INSERT INTO content_keyword_terms VALUES(606,303,'en','working memory','working memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(607,304,'pl','pamięć schematyczna','pamięć schematyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(608,304,'en','schematic memory','schematic memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(609,305,'pl','pamięć strukturalna','pamięć strukturalna',1,NULL);

INSERT INTO content_keyword_terms VALUES(610,305,'en','structural memory','structural memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(611,306,'pl','pamięć wskaźnikowa','pamięć wskaźnikowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(612,306,'en','pointer-based memory','pointer-based memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(613,307,'pl','pamięć zewnętrzna','pamięć zewnętrzna',1,NULL);

INSERT INTO content_keyword_terms VALUES(614,307,'en','external memory','external memory',1,NULL);

INSERT INTO content_keyword_terms VALUES(615,308,'pl','pamiętanie o drugiej osobie','pamiętanie o drugiej osobie',1,NULL);

INSERT INTO content_keyword_terms VALUES(616,308,'en','remembering others','remembering others',1,NULL);

INSERT INTO content_keyword_terms VALUES(617,309,'pl','paradoks porządku i chaosu','paradoks porządku i chaosu',1,NULL);

INSERT INTO content_keyword_terms VALUES(618,309,'en','order–chaos paradox','order–chaos paradox',1,NULL);

INSERT INTO content_keyword_terms VALUES(619,310,'pl','parafraza','parafraza',1,NULL);

INSERT INTO content_keyword_terms VALUES(620,310,'en','paraphrase','paraphrase',1,NULL);

INSERT INTO content_keyword_terms VALUES(621,311,'pl','paraliż','paraliż',1,NULL);

INSERT INTO content_keyword_terms VALUES(622,311,'en','paralysis','paralysis',1,NULL);

INSERT INTO content_keyword_terms VALUES(623,312,'pl','para ND','para nd',1,NULL);

INSERT INTO content_keyword_terms VALUES(624,312,'en','neurodivergent couple','neurodivergent couple',1,NULL);

INSERT INTO content_keyword_terms VALUES(625,313,'pl','para ND-NT','para nd-nt',1,NULL);

INSERT INTO content_keyword_terms VALUES(626,313,'en','neurodivergent–neurotypical couple','neurodivergent–neurotypical couple',1,NULL);

INSERT INTO content_keyword_terms VALUES(627,314,'pl','partycypacja','partycypacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(628,314,'en','participation','participation',1,NULL);

INSERT INTO content_keyword_terms VALUES(629,315,'pl','patologizacja','patologizacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(630,315,'en','pathologization','pathologization',1,NULL);

INSERT INTO content_keyword_terms VALUES(631,316,'pl','percepcja','percepcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(632,316,'en','perception','perception',1,NULL);

INSERT INTO content_keyword_terms VALUES(633,317,'pl','perfekcjonizm','perfekcjonizm',1,NULL);

INSERT INTO content_keyword_terms VALUES(634,317,'en','perfectionism','perfectionism',1,NULL);

INSERT INTO content_keyword_terms VALUES(635,318,'pl','pęd','pęd',1,NULL);

INSERT INTO content_keyword_terms VALUES(636,318,'en','momentum','momentum',1,NULL);

INSERT INTO content_keyword_terms VALUES(637,319,'pl','pionierzy IT','pionierzy it',1,NULL);

INSERT INTO content_keyword_terms VALUES(638,319,'en','information technology pioneers','information technology pioneers',1,NULL);

INSERT INTO content_keyword_terms VALUES(639,320,'pl','planowanie','planowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(640,320,'en','planning','planning',1,NULL);

INSERT INTO content_keyword_terms VALUES(641,321,'pl','pliki','pliki',1,NULL);

INSERT INTO content_keyword_terms VALUES(642,321,'en','files','files',1,NULL);

INSERT INTO content_keyword_terms VALUES(643,322,'pl','pobudzenie poznawcze','pobudzenie poznawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(644,322,'en','cognitive arousal','cognitive arousal',1,NULL);

INSERT INTO content_keyword_terms VALUES(645,323,'pl','pochodzenie informacji','pochodzenie informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(646,323,'en','information provenance','information provenance',1,NULL);

INSERT INTO content_keyword_terms VALUES(647,324,'pl','poczucie inności','poczucie inności',1,NULL);

INSERT INTO content_keyword_terms VALUES(648,324,'en','sense of otherness','sense of otherness',1,NULL);

INSERT INTO content_keyword_terms VALUES(649,325,'pl','poczucie udawania dorosłego','poczucie udawania dorosłego',1,NULL);

INSERT INTO content_keyword_terms VALUES(650,325,'en','adult-role impostor feelings','adult-role impostor feelings',1,NULL);

INSERT INTO content_keyword_terms VALUES(651,326,'pl','poczucie winy','poczucie winy',1,NULL);

INSERT INTO content_keyword_terms VALUES(652,326,'en','guilt','guilt',1,NULL);

INSERT INTO content_keyword_terms VALUES(653,327,'pl','poczucie za dużo i za mało','poczucie za dużo i za mało',1,NULL);

INSERT INTO content_keyword_terms VALUES(654,327,'en','perceived excess and inadequacy','perceived excess and inadequacy',1,NULL);

INSERT INTO content_keyword_terms VALUES(655,328,'pl','podwójna empatia','podwójna empatia',1,NULL);

INSERT INTO content_keyword_terms VALUES(656,328,'en','double empathy problem','double empathy problem',1,NULL);

INSERT INTO content_keyword_terms VALUES(657,329,'pl','podwójne przetwarzanie','podwójne przetwarzanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(658,329,'en','dual processing','dual processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(659,330,'pl','pole elektromagnetyczne','pole elektromagnetyczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(660,330,'en','electromagnetic field','electromagnetic field',1,NULL);

INSERT INTO content_keyword_terms VALUES(661,331,'pl','Polska','polska',1,NULL);

INSERT INTO content_keyword_terms VALUES(662,331,'en','Poland','poland',1,NULL);

INSERT INTO content_keyword_terms VALUES(663,332,'pl','położenie','położenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(664,332,'en','position','position',1,NULL);

INSERT INTO content_keyword_terms VALUES(665,333,'pl','pomaganie','pomaganie',1,NULL);

INSERT INTO content_keyword_terms VALUES(666,333,'en','helping behavior','helping behavior',1,NULL);

INSERT INTO content_keyword_terms VALUES(667,334,'pl','populacja','populacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(668,334,'en','population','population',1,NULL);

INSERT INTO content_keyword_terms VALUES(669,335,'pl','popularność technologii','popularność technologii',1,NULL);

INSERT INTO content_keyword_terms VALUES(670,335,'en','technology popularity','technology popularity',1,NULL);

INSERT INTO content_keyword_terms VALUES(671,336,'pl','porównanie modeli','porównanie modeli',1,NULL);

INSERT INTO content_keyword_terms VALUES(672,336,'en','model comparison','model comparison',1,NULL);

INSERT INTO content_keyword_terms VALUES(673,337,'pl','poszukiwanie i unikanie bodźców','poszukiwanie i unikanie bodźców',1,NULL);

INSERT INTO content_keyword_terms VALUES(674,337,'en','sensory seeking and avoidance','sensory seeking and avoidance',1,NULL);

INSERT INTO content_keyword_terms VALUES(675,338,'pl','poszukiwanie sensoryczne','poszukiwanie sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(676,338,'en','sensory seeking','sensory seeking',1,NULL);

INSERT INTO content_keyword_terms VALUES(677,339,'pl','potrzeba nowości','potrzeba nowości',1,NULL);

INSERT INTO content_keyword_terms VALUES(678,339,'en','novelty seeking','novelty seeking',1,NULL);

INSERT INTO content_keyword_terms VALUES(679,340,'pl','potrzeba pomagania','potrzeba pomagania',1,NULL);

INSERT INTO content_keyword_terms VALUES(680,340,'en','need to help','need to help',1,NULL);

INSERT INTO content_keyword_terms VALUES(681,341,'pl','potrzeba rozumienia dlaczego','potrzeba rozumienia dlaczego',1,NULL);

INSERT INTO content_keyword_terms VALUES(682,341,'en','need for explanatory understanding','need for explanatory understanding',1,NULL);

INSERT INTO content_keyword_terms VALUES(683,342,'pl','potrzeba samotności','potrzeba samotności',1,NULL);

INSERT INTO content_keyword_terms VALUES(684,342,'en','need for solitude','need for solitude',1,NULL);

INSERT INTO content_keyword_terms VALUES(685,343,'pl','potrzeba struktury','potrzeba struktury',1,NULL);

INSERT INTO content_keyword_terms VALUES(686,343,'en','need for structure','need for structure',1,NULL);

INSERT INTO content_keyword_terms VALUES(687,344,'pl','potrzeby po diagnozie','potrzeby po diagnozie',1,NULL);

INSERT INTO content_keyword_terms VALUES(688,344,'en','post-diagnostic needs','post-diagnostic needs',1,NULL);

INSERT INTO content_keyword_terms VALUES(689,345,'pl','potwierdzenie zasad relacji','potwierdzenie zasad relacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(690,345,'en','explicit relationship-rule confirmation','explicit relationship-rule confirmation',1,NULL);

INSERT INTO content_keyword_terms VALUES(691,346,'pl','powtarzalność','powtarzalność',1,NULL);

INSERT INTO content_keyword_terms VALUES(692,346,'en','repetitiveness','repetitiveness',1,NULL);

INSERT INTO content_keyword_terms VALUES(693,347,'pl','poznanie społeczne','poznanie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(694,347,'en','social cognition','social cognition',1,NULL);

INSERT INTO content_keyword_terms VALUES(695,348,'pl','późna diagnoza','późna diagnoza',1,NULL);

INSERT INTO content_keyword_terms VALUES(696,348,'en','late diagnosis','late diagnosis',1,NULL);

INSERT INTO content_keyword_terms VALUES(697,349,'pl','pragmatyka','pragmatyka',1,NULL);

INSERT INTO content_keyword_terms VALUES(698,349,'en','pragmatics','pragmatics',1,NULL);

INSERT INTO content_keyword_terms VALUES(699,350,'pl','prawdopodobieństwo warunkowe','prawdopodobieństwo warunkowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(700,350,'en','conditional probability','conditional probability',1,NULL);

INSERT INTO content_keyword_terms VALUES(701,351,'pl','predyspozycje','predyspozycje',1,NULL);

INSERT INTO content_keyword_terms VALUES(702,351,'en','predispositions','predispositions',1,NULL);

INSERT INTO content_keyword_terms VALUES(703,352,'pl','presja społeczna','presja społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(704,352,'en','social pressure','social pressure',1,NULL);

INSERT INTO content_keyword_terms VALUES(705,353,'pl','prezent','prezent',1,NULL);

INSERT INTO content_keyword_terms VALUES(706,353,'en','gift','gift',1,NULL);

INSERT INTO content_keyword_terms VALUES(707,354,'pl','procedura','procedura',1,NULL);

INSERT INTO content_keyword_terms VALUES(708,354,'en','procedure','procedure',1,NULL);

INSERT INTO content_keyword_terms VALUES(709,355,'pl','programowanie','programowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(710,355,'en','programming','programming',1,NULL);

INSERT INTO content_keyword_terms VALUES(711,356,'pl','programowanie niskopoziomowe','programowanie niskopoziomowe',1,NULL);

INSERT INTO content_keyword_terms VALUES(712,356,'en','low-level programming','low-level programming',1,NULL);

INSERT INTO content_keyword_terms VALUES(713,357,'pl','projektowanie języków','projektowanie języków',1,NULL);

INSERT INTO content_keyword_terms VALUES(714,357,'en','programming language design','programming language design',1,NULL);

INSERT INTO content_keyword_terms VALUES(715,358,'pl','projektowanie promptów','projektowanie promptów',1,NULL);

INSERT INTO content_keyword_terms VALUES(716,358,'en','prompt engineering','prompt engineering',1,NULL);

INSERT INTO content_keyword_terms VALUES(717,359,'pl','projektowanie systemów','projektowanie systemów',1,NULL);

INSERT INTO content_keyword_terms VALUES(718,359,'en','systems design','systems design',1,NULL);

INSERT INTO content_keyword_terms VALUES(719,360,'pl','projekty','projekty',1,NULL);

INSERT INTO content_keyword_terms VALUES(720,360,'en','projects','projects',1,NULL);

INSERT INTO content_keyword_terms VALUES(721,361,'pl','prokrastynacja','prokrastynacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(722,361,'en','procrastination','procrastination',1,NULL);

INSERT INTO content_keyword_terms VALUES(723,362,'pl','prokrastynacja perfekcjonistyczna','prokrastynacja perfekcjonistyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(724,362,'en','perfectionism-related procrastination','perfectionism-related procrastination',1,NULL);

INSERT INTO content_keyword_terms VALUES(725,363,'pl','propriocepcja','propriocepcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(726,363,'en','proprioception','proprioception',1,NULL);

INSERT INTO content_keyword_terms VALUES(727,364,'pl','propriocepcja i koordynacja','propriocepcja i koordynacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(728,364,'en','proprioception and coordination','proprioception and coordination',1,NULL);

INSERT INTO content_keyword_terms VALUES(729,365,'pl','prowadzący neuroróżnorodny','prowadzący neuroróżnorodny',1,NULL);

INSERT INTO content_keyword_terms VALUES(730,365,'en','neurodivergent facilitator','neurodivergent facilitator',1,NULL);

INSERT INTO content_keyword_terms VALUES(731,366,'pl','przeciążenie','przeciążenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(732,366,'en','overload','overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(733,367,'pl','przeciążenie informacyjne','przeciążenie informacyjne',1,NULL);

INSERT INTO content_keyword_terms VALUES(734,367,'en','information overload','information overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(735,368,'pl','przeciążenie poznawcze','przeciążenie poznawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(736,368,'en','cognitive overload','cognitive overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(737,369,'pl','przeciążenie sensoryczne','przeciążenie sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(738,369,'en','sensory overload','sensory overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(739,370,'pl','przeciążenie społeczne','przeciążenie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(740,370,'en','social overload','social overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(741,371,'pl','przeciążenie wykonawcze','przeciążenie wykonawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(742,371,'en','executive overload','executive overload',1,NULL);

INSERT INTO content_keyword_terms VALUES(743,372,'pl','przeglądarki','przeglądarki',1,NULL);

INSERT INTO content_keyword_terms VALUES(744,372,'en','web browsers','web browsers',1,NULL);

INSERT INTO content_keyword_terms VALUES(745,373,'pl','przejrzystość','przejrzystość',1,NULL);

INSERT INTO content_keyword_terms VALUES(746,373,'en','transparency','transparency',1,NULL);

INSERT INTO content_keyword_terms VALUES(747,374,'pl','przełączanie zadań','przełączanie zadań',1,NULL);

INSERT INTO content_keyword_terms VALUES(748,374,'en','task switching','task switching',1,NULL);

INSERT INTO content_keyword_terms VALUES(749,375,'pl','przepływ','przepływ',1,NULL);

INSERT INTO content_keyword_terms VALUES(750,375,'en','flow','flow',1,NULL);

INSERT INTO content_keyword_terms VALUES(751,376,'pl','przetwarzanie informacji','przetwarzanie informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(752,376,'en','information processing','information processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(753,377,'pl','przetwarzanie lokalne','przetwarzanie lokalne',1,NULL);

INSERT INTO content_keyword_terms VALUES(754,377,'en','local processing','local processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(755,378,'pl','przetwarzanie sensoryczne','przetwarzanie sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(756,378,'en','sensory processing','sensory processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(757,379,'pl','przetwarzanie w tle','przetwarzanie w tle',1,NULL);

INSERT INTO content_keyword_terms VALUES(758,379,'en','background processing','background processing',1,NULL);

INSERT INTO content_keyword_terms VALUES(759,380,'pl','przewidywalność','przewidywalność',1,NULL);

INSERT INTO content_keyword_terms VALUES(760,380,'en','predictability','predictability',1,NULL);

INSERT INTO content_keyword_terms VALUES(761,381,'pl','przynależność','przynależność',1,NULL);

INSERT INTO content_keyword_terms VALUES(762,381,'en','belonging','belonging',1,NULL);

INSERT INTO content_keyword_terms VALUES(763,382,'pl','przywoływanie pamięci','przywoływanie pamięci',1,NULL);

INSERT INTO content_keyword_terms VALUES(764,382,'en','memory retrieval','memory retrieval',1,NULL);

INSERT INTO content_keyword_terms VALUES(765,383,'pl','psychodynamika','psychodynamika',1,NULL);

INSERT INTO content_keyword_terms VALUES(766,383,'en','psychodynamics','psychodynamics',1,NULL);

INSERT INTO content_keyword_terms VALUES(767,384,'pl','psychoedukacja','psychoedukacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(768,384,'en','psychoeducation','psychoeducation',1,NULL);

INSERT INTO content_keyword_terms VALUES(769,385,'pl','psychoterapia','psychoterapia',1,NULL);

INSERT INTO content_keyword_terms VALUES(770,385,'en','psychotherapy','psychotherapy',1,NULL);

INSERT INTO content_keyword_terms VALUES(771,386,'pl','punktualność','punktualność',1,NULL);

INSERT INTO content_keyword_terms VALUES(772,386,'en','punctuality','punctuality',1,NULL);

INSERT INTO content_keyword_terms VALUES(773,387,'pl','pustka','pustka',1,NULL);

INSERT INTO content_keyword_terms VALUES(774,387,'en','emptiness','emptiness',1,NULL);

INSERT INTO content_keyword_terms VALUES(775,388,'pl','Python','python',1,NULL);

INSERT INTO content_keyword_terms VALUES(776,388,'en','Python','python',1,NULL);

INSERT INTO content_keyword_terms VALUES(777,389,'pl','RAM','ram',1,NULL);

INSERT INTO content_keyword_terms VALUES(778,389,'en','RAM','ram',1,NULL);

INSERT INTO content_keyword_terms VALUES(779,390,'pl','rdzeń AuDHD','rdzeń audhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(780,390,'en','AuDHD core features','audhd core features',1,NULL);

INSERT INTO content_keyword_terms VALUES(781,391,'pl','refaktoryzacja','refaktoryzacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(782,391,'en','refactoring','refactoring',1,NULL);

INSERT INTO content_keyword_terms VALUES(783,392,'pl','referencje','referencje',1,NULL);

INSERT INTO content_keyword_terms VALUES(784,392,'en','references','references',1,NULL);

INSERT INTO content_keyword_terms VALUES(785,393,'pl','regresja','regresja',1,NULL);

INSERT INTO content_keyword_terms VALUES(786,393,'en','regression','regression',1,NULL);

INSERT INTO content_keyword_terms VALUES(787,394,'pl','regulacja mówienia','regulacja mówienia',1,NULL);

INSERT INTO content_keyword_terms VALUES(788,394,'en','speech regulation','speech regulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(789,395,'pl','regulacja sensoryczna','regulacja sensoryczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(790,395,'en','sensory regulation','sensory regulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(791,396,'pl','reguły społeczne','reguły społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(792,396,'en','social rules','social rules',1,NULL);

INSERT INTO content_keyword_terms VALUES(793,397,'pl','rekonstrukcja','rekonstrukcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(794,397,'en','reconstruction','reconstruction',1,NULL);

INSERT INTO content_keyword_terms VALUES(795,398,'pl','rekursja','rekursja',1,NULL);

INSERT INTO content_keyword_terms VALUES(796,398,'en','recursion','recursion',1,NULL);

INSERT INTO content_keyword_terms VALUES(797,399,'pl','relacje','relacje',1,NULL);

INSERT INTO content_keyword_terms VALUES(798,399,'en','relationships','relationships',1,NULL);

INSERT INTO content_keyword_terms VALUES(799,400,'pl','Richard Stallman','richard stallman',1,NULL);

INSERT INTO content_keyword_terms VALUES(800,400,'en','Richard Stallman','richard stallman',1,NULL);

INSERT INTO content_keyword_terms VALUES(801,401,'pl','rozpoznawanie','rozpoznawanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(802,401,'en','recognition','recognition',1,NULL);

INSERT INTO content_keyword_terms VALUES(803,402,'pl','rozpoznawanie emocji','rozpoznawanie emocji',1,NULL);

INSERT INTO content_keyword_terms VALUES(804,402,'en','emotion recognition','emotion recognition',1,NULL);

INSERT INTO content_keyword_terms VALUES(805,403,'pl','rozpoznawanie wzorców','rozpoznawanie wzorców',1,NULL);

INSERT INTO content_keyword_terms VALUES(806,403,'en','pattern recognition','pattern recognition',1,NULL);

INSERT INTO content_keyword_terms VALUES(807,404,'pl','rozwiązywanie problemów','rozwiązywanie problemów',1,NULL);

INSERT INTO content_keyword_terms VALUES(808,404,'en','problem solving','problem solving',1,NULL);

INSERT INTO content_keyword_terms VALUES(809,405,'pl','równania fundamentalne','równania fundamentalne',1,NULL);

INSERT INTO content_keyword_terms VALUES(810,405,'en','fundamental equations','fundamental equations',1,NULL);

INSERT INTO content_keyword_terms VALUES(811,406,'pl','równania Maxwella','równania maxwella',1,NULL);

INSERT INTO content_keyword_terms VALUES(812,406,'en','Maxwell''s equations','maxwell''s equations',1,NULL);

INSERT INTO content_keyword_terms VALUES(813,407,'pl','równania Naviera–Stokesa','równania naviera–stokesa',1,NULL);

INSERT INTO content_keyword_terms VALUES(814,407,'en','Navier–Stokes equations','navier–stokes equations',1,NULL);

INSERT INTO content_keyword_terms VALUES(815,408,'pl','równanie Diraca','równanie diraca',1,NULL);

INSERT INTO content_keyword_terms VALUES(816,408,'en','Dirac equation','dirac equation',1,NULL);

INSERT INTO content_keyword_terms VALUES(817,409,'pl','równoległa obecność','równoległa obecność',1,NULL);

INSERT INTO content_keyword_terms VALUES(818,409,'en','parallel play','parallel play',1,NULL);

INSERT INTO content_keyword_terms VALUES(819,410,'pl','rutyna','rutyna',1,NULL);

INSERT INTO content_keyword_terms VALUES(820,410,'en','routine','routine',1,NULL);

INSERT INTO content_keyword_terms VALUES(821,411,'pl','rynek terapeutyczny','rynek terapeutyczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(822,411,'en','therapy market','therapy market',1,NULL);

INSERT INTO content_keyword_terms VALUES(823,412,'pl','rytm dobowy','rytm dobowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(824,412,'en','circadian rhythm','circadian rhythm',1,NULL);

INSERT INTO content_keyword_terms VALUES(825,413,'pl','ryzyko terapii','ryzyko terapii',1,NULL);

INSERT INTO content_keyword_terms VALUES(826,413,'en','treatment risk','treatment risk',1,NULL);

INSERT INTO content_keyword_terms VALUES(827,414,'pl','samokontrola','samokontrola',1,NULL);

INSERT INTO content_keyword_terms VALUES(828,414,'en','self-control','self-control',1,NULL);

INSERT INTO content_keyword_terms VALUES(829,415,'pl','samoocena','samoocena',1,NULL);

INSERT INTO content_keyword_terms VALUES(830,415,'en','self-esteem','self-esteem',1,NULL);

INSERT INTO content_keyword_terms VALUES(831,416,'pl','samoodwołanie','samoodwołanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(832,416,'en','self-reference','self-reference',1,NULL);

INSERT INTO content_keyword_terms VALUES(833,417,'pl','samopomoc','samopomoc',1,NULL);

INSERT INTO content_keyword_terms VALUES(834,417,'en','self-help','self-help',1,NULL);

INSERT INTO content_keyword_terms VALUES(835,418,'pl','samopoświęcenie','samopoświęcenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(836,418,'en','self-sacrifice','self-sacrifice',1,NULL);

INSERT INTO content_keyword_terms VALUES(837,419,'pl','samoregulacja','samoregulacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(838,419,'en','self-regulation','self-regulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(839,420,'pl','samowiedza','samowiedza',1,NULL);

INSERT INTO content_keyword_terms VALUES(840,420,'en','self-knowledge','self-knowledge',1,NULL);

INSERT INTO content_keyword_terms VALUES(841,421,'pl','schematy','schematy',1,NULL);

INSERT INTO content_keyword_terms VALUES(842,421,'en','schemas','schemas',1,NULL);

INSERT INTO content_keyword_terms VALUES(843,422,'pl','selekcja zawodowa','selekcja zawodowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(844,422,'en','occupational selection','occupational selection',1,NULL);

INSERT INTO content_keyword_terms VALUES(845,423,'pl','sen','sen',1,NULL);

INSERT INTO content_keyword_terms VALUES(846,423,'en','sleep','sleep',1,NULL);

INSERT INTO content_keyword_terms VALUES(847,424,'pl','sen głęboki','sen głęboki',1,NULL);

INSERT INTO content_keyword_terms VALUES(848,424,'en','deep sleep','deep sleep',1,NULL);

INSERT INTO content_keyword_terms VALUES(849,425,'pl','sen REM','sen rem',1,NULL);

INSERT INTO content_keyword_terms VALUES(850,425,'en','REM sleep','rem sleep',1,NULL);

INSERT INTO content_keyword_terms VALUES(851,426,'pl','separacja danych','separacja danych',1,NULL);

INSERT INTO content_keyword_terms VALUES(852,426,'en','data separation','data separation',1,NULL);

INSERT INTO content_keyword_terms VALUES(853,427,'pl','separacja domen','separacja domen',1,NULL);

INSERT INTO content_keyword_terms VALUES(854,427,'en','domain separation','domain separation',1,NULL);

INSERT INTO content_keyword_terms VALUES(855,428,'pl','separacja kontekstu','separacja kontekstu',1,NULL);

INSERT INTO content_keyword_terms VALUES(856,428,'en','context separation','context separation',1,NULL);

INSERT INTO content_keyword_terms VALUES(857,429,'pl','sieć wsparcia','sieć wsparcia',1,NULL);

INSERT INTO content_keyword_terms VALUES(858,429,'en','support network','support network',1,NULL);

INSERT INTO content_keyword_terms VALUES(859,430,'pl','skalowalność','skalowalność',1,NULL);

INSERT INTO content_keyword_terms VALUES(860,430,'en','scalability','scalability',1,NULL);

INSERT INTO content_keyword_terms VALUES(861,431,'pl','skalowanie społeczne','skalowanie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(862,431,'en','social scaling','social scaling',1,NULL);

INSERT INTO content_keyword_terms VALUES(863,432,'pl','skażenie informacji','skażenie informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(864,432,'en','information contamination','information contamination',1,NULL);

INSERT INTO content_keyword_terms VALUES(865,433,'pl','skład komputerowy','skład komputerowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(866,433,'en','computer configuration','computer configuration',1,NULL);

INSERT INTO content_keyword_terms VALUES(867,434,'pl','skojarzenia','skojarzenia',1,NULL);

INSERT INTO content_keyword_terms VALUES(868,434,'en','associations','associations',1,NULL);

INSERT INTO content_keyword_terms VALUES(869,435,'pl','skrupulatność moralna','skrupulatność moralna',1,NULL);

INSERT INTO content_keyword_terms VALUES(870,435,'en','moral scrupulosity','moral scrupulosity',1,NULL);

INSERT INTO content_keyword_terms VALUES(871,436,'pl','skuteczność terapii','skuteczność terapii',1,NULL);

INSERT INTO content_keyword_terms VALUES(872,436,'en','treatment efficacy','treatment efficacy',1,NULL);

INSERT INTO content_keyword_terms VALUES(873,437,'pl','słaba interocepcja','słaba interocepcja',1,NULL);

INSERT INTO content_keyword_terms VALUES(874,437,'en','poor interoception','poor interoception',1,NULL);

INSERT INTO content_keyword_terms VALUES(875,438,'pl','specjalizacja','specjalizacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(876,438,'en','specialization','specialization',1,NULL);

INSERT INTO content_keyword_terms VALUES(877,439,'pl','specyficzny humor','specyficzny humor',1,NULL);

INSERT INTO content_keyword_terms VALUES(878,439,'en','distinctive humor','distinctive humor',1,NULL);

INSERT INTO content_keyword_terms VALUES(879,440,'pl','spin','spin',1,NULL);

INSERT INTO content_keyword_terms VALUES(880,440,'en','spin','spin',1,NULL);

INSERT INTO content_keyword_terms VALUES(881,441,'pl','spójność centralna','spójność centralna',1,NULL);

INSERT INTO content_keyword_terms VALUES(882,441,'en','central coherence','central coherence',1,NULL);

INSERT INTO content_keyword_terms VALUES(883,442,'pl','spójność kontekstu','spójność kontekstu',1,NULL);

INSERT INTO content_keyword_terms VALUES(884,442,'en','contextual coherence','contextual coherence',1,NULL);

INSERT INTO content_keyword_terms VALUES(885,443,'pl','spójność modelu','spójność modelu',1,NULL);

INSERT INTO content_keyword_terms VALUES(886,443,'en','model coherence','model coherence',1,NULL);

INSERT INTO content_keyword_terms VALUES(887,444,'pl','sprawiedliwość','sprawiedliwość',1,NULL);

INSERT INTO content_keyword_terms VALUES(888,444,'en','justice','justice',1,NULL);

INSERT INTO content_keyword_terms VALUES(889,445,'pl','standard informacyjny','standard informacyjny',1,NULL);

INSERT INTO content_keyword_terms VALUES(890,445,'en','information standard','information standard',1,NULL);

INSERT INTO content_keyword_terms VALUES(891,446,'pl','standard wsparcia','standard wsparcia',1,NULL);

INSERT INTO content_keyword_terms VALUES(892,446,'en','support standard','support standard',1,NULL);

INSERT INTO content_keyword_terms VALUES(893,447,'pl','stan przewlekły','stan przewlekły',1,NULL);

INSERT INTO content_keyword_terms VALUES(894,447,'en','chronic condition','chronic condition',1,NULL);

INSERT INTO content_keyword_terms VALUES(895,448,'pl','stereotypy','stereotypy',1,NULL);

INSERT INTO content_keyword_terms VALUES(896,448,'en','stereotypes','stereotypes',1,NULL);

INSERT INTO content_keyword_terms VALUES(897,449,'pl','Steve Wozniak','steve wozniak',1,NULL);

INSERT INTO content_keyword_terms VALUES(898,449,'en','Steve Wozniak','steve wozniak',1,NULL);

INSERT INTO content_keyword_terms VALUES(899,450,'pl','stimming','stimming',1,NULL);

INSERT INTO content_keyword_terms VALUES(900,450,'en','stimming','stimming',1,NULL);

INSERT INTO content_keyword_terms VALUES(901,451,'pl','strategie kompensacyjne','strategie kompensacyjne',1,NULL);

INSERT INTO content_keyword_terms VALUES(902,451,'en','compensatory strategies','compensatory strategies',1,NULL);

INSERT INTO content_keyword_terms VALUES(903,452,'pl','strategie ochronne','strategie ochronne',1,NULL);

INSERT INTO content_keyword_terms VALUES(904,452,'en','protective strategies','protective strategies',1,NULL);

INSERT INTO content_keyword_terms VALUES(905,453,'pl','strategie poznawcze','strategie poznawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(906,453,'en','cognitive strategies','cognitive strategies',1,NULL);

INSERT INTO content_keyword_terms VALUES(907,454,'pl','stres','stres',1,NULL);

INSERT INTO content_keyword_terms VALUES(908,454,'en','stress','stress',1,NULL);

INSERT INTO content_keyword_terms VALUES(909,455,'pl','streszczenia','streszczenia',1,NULL);

INSERT INTO content_keyword_terms VALUES(910,455,'en','summaries','summaries',1,NULL);

INSERT INTO content_keyword_terms VALUES(911,456,'pl','strumień danych','strumień danych',1,NULL);

INSERT INTO content_keyword_terms VALUES(912,456,'en','data stream','data stream',1,NULL);

INSERT INTO content_keyword_terms VALUES(913,457,'pl','styl poznawczy','styl poznawczy',1,NULL);

INSERT INTO content_keyword_terms VALUES(914,457,'en','cognitive style','cognitive style',1,NULL);

INSERT INTO content_keyword_terms VALUES(915,458,'pl','surowe bodźce','surowe bodźce',1,NULL);

INSERT INTO content_keyword_terms VALUES(916,458,'en','raw sensory input','raw sensory input',1,NULL);

INSERT INTO content_keyword_terms VALUES(917,459,'pl','sygnały ciała','sygnały ciała',1,NULL);

INSERT INTO content_keyword_terms VALUES(918,459,'en','bodily signals','bodily signals',1,NULL);

INSERT INTO content_keyword_terms VALUES(919,460,'pl','sygnały społeczne','sygnały społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(920,460,'en','social cues','social cues',1,NULL);

INSERT INTO content_keyword_terms VALUES(921,461,'pl','sygnały zwrotne','sygnały zwrotne',1,NULL);

INSERT INTO content_keyword_terms VALUES(922,461,'en','feedback signals','feedback signals',1,NULL);

INSERT INTO content_keyword_terms VALUES(923,462,'pl','systemy rozproszone','systemy rozproszone',1,NULL);

INSERT INTO content_keyword_terms VALUES(924,462,'en','distributed systems','distributed systems',1,NULL);

INSERT INTO content_keyword_terms VALUES(925,463,'pl','system wsparcia','system wsparcia',1,NULL);

INSERT INTO content_keyword_terms VALUES(926,463,'en','support system','support system',1,NULL);

INSERT INTO content_keyword_terms VALUES(927,464,'pl','szczegóły','szczegóły',1,NULL);

INSERT INTO content_keyword_terms VALUES(928,464,'en','details','details',1,NULL);

INSERT INTO content_keyword_terms VALUES(929,465,'pl','szkoda terapeutyczna','szkoda terapeutyczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(930,465,'en','treatment-related harm','treatment-related harm',1,NULL);

INSERT INTO content_keyword_terms VALUES(931,466,'pl','sztuczna inteligencja','sztuczna inteligencja',1,NULL);

INSERT INTO content_keyword_terms VALUES(932,466,'en','artificial intelligence','artificial intelligence',1,NULL);

INSERT INTO content_keyword_terms VALUES(933,467,'pl','sztywność poznawcza','sztywność poznawcza',1,NULL);

INSERT INTO content_keyword_terms VALUES(934,467,'en','cognitive rigidity','cognitive rigidity',1,NULL);

INSERT INTO content_keyword_terms VALUES(935,468,'pl','ślepota czasowa','ślepota czasowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(936,468,'en','time blindness','time blindness',1,NULL);

INSERT INTO content_keyword_terms VALUES(937,469,'pl','środowisko społeczne','środowisko społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(938,469,'en','social environment','social environment',1,NULL);

INSERT INTO content_keyword_terms VALUES(939,470,'pl','świadomość','świadomość',1,NULL);

INSERT INTO content_keyword_terms VALUES(940,470,'en','awareness','awareness',1,NULL);

INSERT INTO content_keyword_terms VALUES(941,471,'pl','świadomość ciała','świadomość ciała',1,NULL);

INSERT INTO content_keyword_terms VALUES(942,471,'en','body awareness','body awareness',1,NULL);

INSERT INTO content_keyword_terms VALUES(943,472,'pl','świadomość neuroróżnorodności','świadomość neuroróżnorodności',1,NULL);

INSERT INTO content_keyword_terms VALUES(944,472,'en','neurodiversity awareness','neurodiversity awareness',1,NULL);

INSERT INTO content_keyword_terms VALUES(945,473,'pl','terapeuci ND','terapeuci nd',1,NULL);

INSERT INTO content_keyword_terms VALUES(946,473,'en','neurodivergent therapists','neurodivergent therapists',1,NULL);

INSERT INTO content_keyword_terms VALUES(947,474,'pl','terapeuta','terapeuta',1,NULL);

INSERT INTO content_keyword_terms VALUES(948,474,'en','therapist','therapist',1,NULL);

INSERT INTO content_keyword_terms VALUES(949,475,'pl','terapia','terapia',1,NULL);

INSERT INTO content_keyword_terms VALUES(950,475,'en','therapy','therapy',1,NULL);

INSERT INTO content_keyword_terms VALUES(951,476,'pl','terapia schematów','terapia schematów',1,NULL);

INSERT INTO content_keyword_terms VALUES(952,476,'en','schema therapy','schema therapy',1,NULL);

INSERT INTO content_keyword_terms VALUES(953,477,'pl','termodynamika','termodynamika',1,NULL);

INSERT INTO content_keyword_terms VALUES(954,477,'en','thermodynamics','thermodynamics',1,NULL);

INSERT INTO content_keyword_terms VALUES(955,478,'pl','termodynamika informacji','termodynamika informacji',1,NULL);

INSERT INTO content_keyword_terms VALUES(956,478,'en','information thermodynamics','information thermodynamics',1,NULL);

INSERT INTO content_keyword_terms VALUES(957,479,'pl','TeX','tex',1,NULL);

INSERT INTO content_keyword_terms VALUES(958,479,'en','TeX','tex',1,NULL);

INSERT INTO content_keyword_terms VALUES(959,480,'pl','tożsamość','tożsamość',1,NULL);

INSERT INTO content_keyword_terms VALUES(960,480,'en','identity','identity',1,NULL);

INSERT INTO content_keyword_terms VALUES(961,481,'pl','trafność','trafność',1,NULL);

INSERT INTO content_keyword_terms VALUES(962,481,'en','validity','validity',1,NULL);

INSERT INTO content_keyword_terms VALUES(963,482,'pl','transformer','transformer',1,NULL);

INSERT INTO content_keyword_terms VALUES(964,482,'en','transformer','transformer',1,NULL);

INSERT INTO content_keyword_terms VALUES(965,483,'pl','turbulencja','turbulencja',1,NULL);

INSERT INTO content_keyword_terms VALUES(966,483,'en','turbulence','turbulence',1,NULL);

INSERT INTO content_keyword_terms VALUES(967,484,'pl','twórcy technologii','twórcy technologii',1,NULL);

INSERT INTO content_keyword_terms VALUES(968,484,'en','technology creators','technology creators',1,NULL);

INSERT INTO content_keyword_terms VALUES(969,485,'pl','układ nerwowy','układ nerwowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(970,485,'en','nervous system','nervous system',1,NULL);

INSERT INTO content_keyword_terms VALUES(971,486,'pl','układ przedsionkowy','układ przedsionkowy',1,NULL);

INSERT INTO content_keyword_terms VALUES(972,486,'en','vestibular system','vestibular system',1,NULL);

INSERT INTO content_keyword_terms VALUES(973,487,'pl','ulga','ulga',1,NULL);

INSERT INTO content_keyword_terms VALUES(974,487,'en','relief','relief',1,NULL);

INSERT INTO content_keyword_terms VALUES(975,488,'pl','underachievement','underachievement',1,NULL);

INSERT INTO content_keyword_terms VALUES(976,488,'en','underachievement','underachievement',1,NULL);

INSERT INTO content_keyword_terms VALUES(977,489,'pl','unikanie sensoryczne','unikanie sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(978,489,'en','sensory avoidance','sensory avoidance',1,NULL);

INSERT INTO content_keyword_terms VALUES(979,490,'pl','unikanie wymagań','unikanie wymagań',1,NULL);

INSERT INTO content_keyword_terms VALUES(980,490,'en','demand avoidance','demand avoidance',1,NULL);

INSERT INTO content_keyword_terms VALUES(981,491,'pl','Unix','unix',1,NULL);

INSERT INTO content_keyword_terms VALUES(982,491,'en','Unix','unix',1,NULL);

INSERT INTO content_keyword_terms VALUES(983,492,'pl','uwaga','uwaga',1,NULL);

INSERT INTO content_keyword_terms VALUES(984,492,'en','attention','attention',1,NULL);

INSERT INTO content_keyword_terms VALUES(985,493,'pl','uzależnienia','uzależnienia',1,NULL);

INSERT INTO content_keyword_terms VALUES(986,493,'en','addiction','addiction',1,NULL);

INSERT INTO content_keyword_terms VALUES(987,494,'pl','walidacja społeczna','walidacja społeczna',1,NULL);

INSERT INTO content_keyword_terms VALUES(988,494,'en','social validation','social validation',1,NULL);

INSERT INTO content_keyword_terms VALUES(989,495,'pl','walidacja wewnętrzna','walidacja wewnętrzna',1,NULL);

INSERT INTO content_keyword_terms VALUES(990,495,'en','internal validation','internal validation',1,NULL);

INSERT INTO content_keyword_terms VALUES(991,496,'pl','walidacja zewnętrzna','walidacja zewnętrzna',1,NULL);

INSERT INTO content_keyword_terms VALUES(992,496,'en','external validation','external validation',1,NULL);

INSERT INTO content_keyword_terms VALUES(993,497,'pl','wariacja','wariacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(994,497,'en','variation','variation',1,NULL);

INSERT INTO content_keyword_terms VALUES(995,498,'pl','werbalizacja','werbalizacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(996,498,'en','verbalization','verbalization',1,NULL);

INSERT INTO content_keyword_terms VALUES(997,499,'pl','weryfikacja','weryfikacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(998,499,'en','verification','verification',1,NULL);

INSERT INTO content_keyword_terms VALUES(999,500,'pl','wewnętrzny tłumacz społeczny','wewnętrzny tłumacz społeczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(1000,500,'en','internal social interpreter','internal social interpreter',1,NULL);

INSERT INTO content_keyword_terms VALUES(1001,501,'pl','Wheeler–DeWitt','wheeler–dewitt',1,NULL);

INSERT INTO content_keyword_terms VALUES(1002,501,'en','Wheeler–DeWitt equation','wheeler–dewitt equation',1,NULL);

INSERT INTO content_keyword_terms VALUES(1003,502,'pl','wieczorne pobudzenie','wieczorne pobudzenie',1,NULL);

INSERT INTO content_keyword_terms VALUES(1004,502,'en','evening arousal','evening arousal',1,NULL);

INSERT INTO content_keyword_terms VALUES(1005,503,'pl','więź','więź',1,NULL);

INSERT INTO content_keyword_terms VALUES(1006,503,'en','attachment','attachment',1,NULL);

INSERT INTO content_keyword_terms VALUES(1007,504,'pl','wolne oprogramowanie','wolne oprogramowanie',1,NULL);

INSERT INTO content_keyword_terms VALUES(1008,504,'en','free software','free software',1,NULL);

INSERT INTO content_keyword_terms VALUES(1009,505,'pl','wpływ społeczny','wpływ społeczny',1,NULL);

INSERT INTO content_keyword_terms VALUES(1010,505,'en','social influence','social influence',1,NULL);

INSERT INTO content_keyword_terms VALUES(1011,506,'pl','wrażliwość na niesprawiedliwość','wrażliwość na niesprawiedliwość',1,NULL);

INSERT INTO content_keyword_terms VALUES(1012,506,'en','sensitivity to injustice','sensitivity to injustice',1,NULL);

INSERT INTO content_keyword_terms VALUES(1013,507,'pl','wrażliwość na odrzucenie (RSD)','wrażliwość na odrzucenie (rsd)',1,NULL);

INSERT INTO content_keyword_terms VALUES(1014,507,'en','rejection sensitivity','rejection sensitivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(1015,508,'pl','wskaźniki','wskaźniki',1,NULL);

INSERT INTO content_keyword_terms VALUES(1016,508,'en','indicators','indicators',1,NULL);

INSERT INTO content_keyword_terms VALUES(1017,509,'pl','wsparcie','wsparcie',1,NULL);

INSERT INTO content_keyword_terms VALUES(1018,509,'en','support','support',1,NULL);

INSERT INTO content_keyword_terms VALUES(1019,510,'pl','wsparcie po diagnozie','wsparcie po diagnozie',1,NULL);

INSERT INTO content_keyword_terms VALUES(1020,510,'en','post-diagnostic support','post-diagnostic support',1,NULL);

INSERT INTO content_keyword_terms VALUES(1021,511,'pl','wsparcie praktyczne','wsparcie praktyczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1022,511,'en','practical support','practical support',1,NULL);

INSERT INTO content_keyword_terms VALUES(1023,512,'pl','wsparcie rówieśnicze','wsparcie rówieśnicze',1,NULL);

INSERT INTO content_keyword_terms VALUES(1024,512,'en','peer support','peer support',1,NULL);

INSERT INTO content_keyword_terms VALUES(1025,513,'pl','wsparcie społeczne','wsparcie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1026,513,'en','social support','social support',1,NULL);

INSERT INTO content_keyword_terms VALUES(1027,514,'pl','wspólnota rówieśnicza','wspólnota rówieśnicza',1,NULL);

INSERT INTO content_keyword_terms VALUES(1028,514,'en','peer community','peer community',1,NULL);

INSERT INTO content_keyword_terms VALUES(1029,515,'pl','wspólny kod','wspólny kod',1,NULL);

INSERT INTO content_keyword_terms VALUES(1030,515,'en','shared code','shared code',1,NULL);

INSERT INTO content_keyword_terms VALUES(1031,516,'pl','współwystępowanie autyzmu i ADHD','współwystępowanie autyzmu i adhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(1032,516,'en','co-occurring autism and ADHD','co-occurring autism and adhd',1,NULL);

INSERT INTO content_keyword_terms VALUES(1033,517,'pl','wstyd','wstyd',1,NULL);

INSERT INTO content_keyword_terms VALUES(1034,517,'en','shame','shame',1,NULL);

INSERT INTO content_keyword_terms VALUES(1035,518,'pl','wybiórczość pokarmowa','wybiórczość pokarmowa',1,NULL);

INSERT INTO content_keyword_terms VALUES(1036,518,'en','food selectivity','food selectivity',1,NULL);

INSERT INTO content_keyword_terms VALUES(1037,519,'pl','wybór terapeuty','wybór terapeuty',1,NULL);

INSERT INTO content_keyword_terms VALUES(1038,519,'en','therapist selection','therapist selection',1,NULL);

INSERT INTO content_keyword_terms VALUES(1039,520,'pl','wykorzystywanie społeczne','wykorzystywanie społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1040,520,'en','social exploitation','social exploitation',1,NULL);

INSERT INTO content_keyword_terms VALUES(1041,521,'pl','wyobraźnia','wyobraźnia',1,NULL);

INSERT INTO content_keyword_terms VALUES(1042,521,'en','imagination','imagination',1,NULL);

INSERT INTO content_keyword_terms VALUES(1043,522,'pl','wypalenie autystyczne','wypalenie autystyczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1044,522,'en','autistic burnout','autistic burnout',1,NULL);

INSERT INTO content_keyword_terms VALUES(1045,523,'pl','wzajemna pomoc','wzajemna pomoc',1,NULL);

INSERT INTO content_keyword_terms VALUES(1046,523,'en','mutual aid','mutual aid',1,NULL);

INSERT INTO content_keyword_terms VALUES(1047,524,'pl','względność','względność',1,NULL);

INSERT INTO content_keyword_terms VALUES(1048,524,'en','relativity','relativity',1,NULL);

INSERT INTO content_keyword_terms VALUES(1049,525,'pl','wzorce funkcjonowania','wzorce funkcjonowania',1,NULL);

INSERT INTO content_keyword_terms VALUES(1050,525,'en','patterns of functioning','patterns of functioning',1,NULL);

INSERT INTO content_keyword_terms VALUES(1051,526,'pl','zaburzenia snu','zaburzenia snu',1,NULL);

INSERT INTO content_keyword_terms VALUES(1052,526,'en','sleep disorders','sleep disorders',1,NULL);

INSERT INTO content_keyword_terms VALUES(1053,527,'pl','zachowania społeczne','zachowania społeczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1054,527,'en','social behavior','social behavior',1,NULL);

INSERT INTO content_keyword_terms VALUES(1055,528,'pl','zadania','zadania',1,NULL);

INSERT INTO content_keyword_terms VALUES(1056,528,'en','tasks','tasks',1,NULL);

INSERT INTO content_keyword_terms VALUES(1057,529,'pl','zainteresowania specjalne','zainteresowania specjalne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1058,529,'en','special interests','special interests',1,NULL);

INSERT INTO content_keyword_terms VALUES(1059,530,'pl','zarządzanie czasem','zarządzanie czasem',1,NULL);

INSERT INTO content_keyword_terms VALUES(1060,530,'en','time management','time management',1,NULL);

INSERT INTO content_keyword_terms VALUES(1061,531,'pl','zarządzanie pamięcią','zarządzanie pamięcią',1,NULL);

INSERT INTO content_keyword_terms VALUES(1062,531,'en','memory management','memory management',1,NULL);

INSERT INTO content_keyword_terms VALUES(1063,532,'pl','zasada nieoznaczoności','zasada nieoznaczoności',1,NULL);

INSERT INTO content_keyword_terms VALUES(1064,532,'en','uncertainty principle','uncertainty principle',1,NULL);

INSERT INTO content_keyword_terms VALUES(1065,533,'pl','zasada stacjonarnego działania','zasada stacjonarnego działania',1,NULL);

INSERT INTO content_keyword_terms VALUES(1066,533,'en','principle of stationary action','principle of stationary action',1,NULL);

INSERT INTO content_keyword_terms VALUES(1067,534,'pl','zasoby','zasoby',1,NULL);

INSERT INTO content_keyword_terms VALUES(1068,534,'en','resources','resources',1,NULL);

INSERT INTO content_keyword_terms VALUES(1069,535,'pl','zaufanie do źródeł','zaufanie do źródeł',1,NULL);

INSERT INTO content_keyword_terms VALUES(1070,535,'en','source trust','source trust',1,NULL);

INSERT INTO content_keyword_terms VALUES(1071,536,'pl','zdolności poznawcze','zdolności poznawcze',1,NULL);

INSERT INTO content_keyword_terms VALUES(1072,536,'en','cognitive abilities','cognitive abilities',1,NULL);

INSERT INTO content_keyword_terms VALUES(1073,537,'pl','zdrowie psychiczne','zdrowie psychiczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1074,537,'en','mental health','mental health',1,NULL);

INSERT INTO content_keyword_terms VALUES(1075,538,'pl','zewnętrzna regulacja','zewnętrzna regulacja',1,NULL);

INSERT INTO content_keyword_terms VALUES(1076,538,'en','external regulation','external regulation',1,NULL);

INSERT INTO content_keyword_terms VALUES(1077,539,'pl','zmęczenie decyzyjne','zmęczenie decyzyjne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1078,539,'en','decision fatigue','decision fatigue',1,NULL);

INSERT INTO content_keyword_terms VALUES(1079,540,'pl','zmiana aktywności','zmiana aktywności',1,NULL);

INSERT INTO content_keyword_terms VALUES(1080,540,'en','activity transition','activity transition',1,NULL);

INSERT INTO content_keyword_terms VALUES(1081,541,'pl','zmienne progi sensoryczne','zmienne progi sensoryczne',1,NULL);

INSERT INTO content_keyword_terms VALUES(1082,541,'en','variable sensory thresholds','variable sensory thresholds',1,NULL);

INSERT INTO content_keyword_terms VALUES(1083,542,'pl','zmysły','zmysły',1,NULL);

INSERT INTO content_keyword_terms VALUES(1084,542,'en','sensory modalities','sensory modalities',1,NULL);

INSERT INTO content_keyword_terms VALUES(1085,543,'pl','zrozumienie','zrozumienie',1,NULL);

INSERT INTO content_keyword_terms VALUES(1086,543,'en','understanding','understanding',1,NULL);

INSERT INTO content_keyword_terms VALUES(1087,544,'pl','żałoba','żałoba',1,NULL);

INSERT INTO content_keyword_terms VALUES(1088,544,'en','grief','grief',1,NULL);

INSERT INTO content_keyword_terms VALUES(1089,545,'pl','zombierewizor','zombierewizor',1,1);

INSERT INTO content_keyword_terms VALUES(1090,545,'en','zombie reviewer','zombie reviewer',1,1);

INSERT INTO content_keyword_terms VALUES(1091,546,'pl','pomaganie kosztem siebie','pomaganie kosztem siebie',1,1);

INSERT INTO content_keyword_terms VALUES(1092,546,'en','helping at your own expense','helping at your own expense',1,1);

INSERT INTO content_keyword_terms VALUES(1093,547,'pl','osoba fundatorska','osoba fundatorska',1,1);

INSERT INTO content_keyword_terms VALUES(1094,547,'en','foundational builder','foundational builder',1,1);

INSERT INTO content_keyword_terms VALUES(1095,548,'pl','abstrakcja abstrakcji','abstrakcja abstrakcji',1,1);

INSERT INTO content_keyword_terms VALUES(1096,548,'en','abstraction of abstraction','abstraction of abstraction',1,1);

INSERT INTO content_keyword_terms VALUES(1097,549,'pl','domknięcie wewnętrzne założeń','domknięcie wewnętrzne założeń',1,1);

INSERT INTO content_keyword_terms VALUES(1098,549,'en','internal closure of assumptions','internal closure of assumptions',1,1);

INSERT INTO content_keyword_terms VALUES(1099,550,'pl','folk-taksonomia','folk-taksonomia',1,1);

INSERT INTO content_keyword_terms VALUES(1100,550,'en','folk taxonomy','folk taxonomy',1,1);

INSERT INTO content_keyword_terms VALUES(1101,551,'pl','support swapping','support swapping',1,1);

INSERT INTO content_keyword_terms VALUES(1102,551,'en','support swapping','support swapping',1,1);

INSERT INTO content_keyword_terms VALUES(1103,552,'pl','koszt tłumaczenia','koszt tłumaczenia',1,1);

INSERT INTO content_keyword_terms VALUES(1104,552,'en','translation cost','translation cost',1,1);

INSERT INTO content_keyword_terms VALUES(1105,553,'pl','tabliczka ND-status','tabliczka nd-status',1,1);

INSERT INTO content_keyword_terms VALUES(1106,553,'en','ND-status notice','nd-status notice',1,1);

INSERT INTO content_keyword_terms VALUES(1107,554,'pl','trójkąt spalania','trójkąt spalania',1,1);

INSERT INTO content_keyword_terms VALUES(1108,554,'en','combustion triangle','combustion triangle',1,1);

INSERT INTO content_keyword_terms VALUES(1109,555,'pl','Hanza 2.0','hanza 2.0',1,1);

INSERT INTO content_keyword_terms VALUES(1110,555,'en','Hanseatic League 2.0','hanseatic league 2.0',1,1);

INSERT INTO content_keyword_terms VALUES(1111,556,'pl','Disinfolklore','disinfolklore',1,1);

INSERT INTO content_keyword_terms VALUES(1112,556,'en','Disinfolklore','disinfolklore',1,1);

INSERT INTO content_keyword_terms VALUES(1113,557,'pl','dark legitimacy','dark legitimacy',1,1);

INSERT INTO content_keyword_terms VALUES(1114,557,'en','dark legitimacy','dark legitimacy',1,1);

INSERT INTO content_keyword_terms VALUES(1115,558,'pl','cztery tryby','cztery tryby',1,1);

INSERT INTO content_keyword_terms VALUES(1116,558,'en','four modes','four modes',1,1);

INSERT INTO content_keyword_terms VALUES(1117,559,'pl','asymetria opcjonalności','asymetria opcjonalności',1,1);

INSERT INTO content_keyword_terms VALUES(1118,559,'en','asymmetry of optionality','asymmetry of optionality',1,1);

INSERT INTO content_keyword_terms VALUES(1119,560,'pl','kampania ujawnienia','kampania ujawnienia',1,1);

INSERT INTO content_keyword_terms VALUES(1120,560,'en','reveal campaign','reveal campaign',1,1);

INSERT INTO content_keyword_terms VALUES(1121,561,'pl','long-range sanctions','long-range sanctions',1,1);

INSERT INTO content_keyword_terms VALUES(1122,561,'en','long-range sanctions','long-range sanctions',1,1);

INSERT INTO content_keyword_terms VALUES(1123,562,'pl','kompresja napraw','kompresja napraw',1,1);

INSERT INTO content_keyword_terms VALUES(1124,562,'en','repair compression','repair compression',1,1);

INSERT INTO content_keyword_terms VALUES(1125,563,'pl','wyspa logistyczna','wyspa logistyczna',1,1);

INSERT INTO content_keyword_terms VALUES(1126,563,'en','logistical island','logistical island',1,1);

INSERT INTO content_keyword_terms VALUES(1127,564,'pl','patrymonialny grid lock','patrymonialny grid lock',1,1);

INSERT INTO content_keyword_terms VALUES(1128,564,'en','patrimonial gridlock','patrimonial gridlock',1,1);

INSERT INTO content_keyword_terms VALUES(1129,565,'pl','detekcja absencji','detekcja absencji',1,1);

INSERT INTO content_keyword_terms VALUES(1130,565,'en','absence detection','absence detection',1,1);

INSERT INTO content_keyword_terms VALUES(1131,566,'pl','cascade gradient','cascade gradient',1,1);

INSERT INTO content_keyword_terms VALUES(1132,566,'en','cascade gradient','cascade gradient',1,1);

INSERT INTO content_keyword_terms VALUES(1133,567,'pl','demembranizacja perymetru','demembranizacja perymetru',1,1);

INSERT INTO content_keyword_terms VALUES(1134,567,'en','demembranisation of the perimeter','demembranisation of the perimeter',1,1);

INSERT INTO content_keyword_terms VALUES(1135,568,'pl','sygnalizacja kalendarzem','sygnalizacja kalendarzem',1,1);

INSERT INTO content_keyword_terms VALUES(1136,568,'en','calendar-based signalling','calendar-based signalling',1,1);

INSERT INTO content_keyword_terms VALUES(1137,569,'pl','kaskada paliwowa','kaskada paliwowa',1,1);

INSERT INTO content_keyword_terms VALUES(1138,569,'en','fuel cascade','fuel cascade',1,1);

INSERT INTO content_keyword_terms VALUES(1139,570,'pl','milczenie strategiczne','milczenie strategiczne',1,1);

INSERT INTO content_keyword_terms VALUES(1140,570,'en','strategic silence','strategic silence',1,1);

INSERT INTO content_keyword_terms VALUES(1141,571,'pl','doktryna maksymalizacji eskalacji','doktryna maksymalizacji eskalacji',1,1);

INSERT INTO content_keyword_terms VALUES(1142,571,'en','doctrine of maximising escalation','doctrine of maximising escalation',1,1);

INSERT INTO content_keyword_terms VALUES(1143,572,'pl','zarządzany upadek','zarządzany upadek',1,1);

INSERT INTO content_keyword_terms VALUES(1144,572,'en','managed decline','managed decline',1,1);

INSERT INTO content_keyword_terms VALUES(1145,573,'pl','chiński substytut komponentowy','chiński substytut komponentowy',1,1);

INSERT INTO content_keyword_terms VALUES(1146,573,'en','Chinese component substitute','chinese component substitute',1,1);

INSERT INTO content_keyword_terms VALUES(1147,574,'pl','sankcje kinetyczne','sankcje kinetyczne',1,1);

INSERT INTO content_keyword_terms VALUES(1148,574,'en','kinetic sanctions','kinetic sanctions',1,1);

INSERT INTO content_keyword_terms VALUES(1149,575,'pl','najkrótszy zapalnik','najkrótszy zapalnik',1,1);

INSERT INTO content_keyword_terms VALUES(1150,575,'en','shortest fuse','shortest fuse',1,1);

INSERT INTO content_keyword_terms VALUES(1151,576,'pl','asymetria ograniczeń','asymetria ograniczeń',1,1);

INSERT INTO content_keyword_terms VALUES(1152,576,'en','asymmetry of constraints','asymmetry of constraints',1,1);

INSERT INTO content_keyword_terms VALUES(1153,577,'pl','inwentarz opcji','inwentarz opcji',1,1);

INSERT INTO content_keyword_terms VALUES(1154,577,'en','inventory of options','inventory of options',1,1);

INSERT INTO content_keyword_terms VALUES(1155,578,'pl','zapas kontra strumień','zapas kontra strumień',1,1);

INSERT INTO content_keyword_terms VALUES(1156,578,'en','stock vs flow','stock vs flow',1,1);

INSERT INTO content_keyword_terms VALUES(1157,579,'pl','cebula transportowa','cebula transportowa',1,1);

INSERT INTO content_keyword_terms VALUES(1158,579,'en','transport onion','transport onion',1,1);

INSERT INTO content_keyword_terms VALUES(1159,580,'pl','pułapka jedynego decydenta','pułapka jedynego decydenta',1,1);

INSERT INTO content_keyword_terms VALUES(1160,580,'en','sole decision-maker trap','sole decision-maker trap',1,1);

INSERT INTO content_keyword_terms VALUES(1161,581,'pl','ruch resztkowy','ruch resztkowy',1,1);

INSERT INTO content_keyword_terms VALUES(1162,581,'en','residual move','residual move',1,1);

INSERT INTO content_keyword_terms VALUES(1163,582,'pl','paradoks zapędzenia','paradoks zapędzenia',1,1);

INSERT INTO content_keyword_terms VALUES(1164,582,'en','cornering paradox','cornering paradox',1,1);

INSERT INTO content_keyword_terms VALUES(1165,583,'pl','fenomenologia końca państwa','fenomenologia końca państwa',1,1);

INSERT INTO content_keyword_terms VALUES(1166,583,'en','phenomenology of state ending','phenomenology of state ending',1,1);

INSERT INTO content_keyword_terms VALUES(1167,584,'pl','spoiwo wewnętrzne','spoiwo wewnętrzne',1,1);

INSERT INTO content_keyword_terms VALUES(1168,584,'en','internal binding','internal binding',1,1);

INSERT INTO content_keyword_terms VALUES(1169,585,'pl','czujnik siły','czujnik siły',1,1);

INSERT INTO content_keyword_terms VALUES(1170,585,'en','strength sensor','strength sensor',1,1);

INSERT INTO content_keyword_terms VALUES(1171,586,'pl','Archetypal Disinfolklore Literacy','archetypal disinfolklore literacy',1,1);

INSERT INTO content_keyword_terms VALUES(1172,586,'en','Archetypal Disinfolklore Literacy','archetypal disinfolklore literacy',1,1);

INSERT INTO content_keyword_terms VALUES(1173,587,'pl','Incoming-Outgoing Troll Radars','incoming-outgoing troll radars',1,1);

INSERT INTO content_keyword_terms VALUES(1174,587,'en','Incoming–Outgoing Troll Radars','incoming–outgoing troll radars',1,1);

INSERT INTO content_keyword_terms VALUES(1175,588,'pl','Witch Switch','witch switch',1,1);

INSERT INTO content_keyword_terms VALUES(1176,588,'en','Witch Switch','witch switch',1,1);

INSERT INTO content_keyword_terms VALUES(1177,589,'pl','Re-Archetyping','re-archetyping',1,1);

INSERT INTO content_keyword_terms VALUES(1178,589,'en','Re-Archetyping','re-archetyping',1,1);

INSERT INTO content_keyword_terms VALUES(1179,590,'pl','Data-Resistant Archetypes','data-resistant archetypes',1,1);

INSERT INTO content_keyword_terms VALUES(1180,590,'en','Data-Resistant Archetypes','data-resistant archetypes',1,1);

INSERT INTO content_keyword_terms VALUES(1181,591,'pl','Counter-Disinfolklore','counter-disinfolklore',1,1);

INSERT INTO content_keyword_terms VALUES(1182,591,'en','Counter-Disinfolklore','counter-disinfolklore',1,1);

INSERT INTO content_keyword_terms VALUES(1183,592,'pl','przesłuchanie informacyjne','przesłuchanie informacyjne',1,1);

INSERT INTO content_keyword_terms VALUES(1184,592,'en','informational cross-examination','informational cross-examination',1,1);

INSERT INTO content_keyword_terms VALUES(1185,593,'pl','taksonomia rosyjskiego samobójstwa','taksonomia rosyjskiego samobójstwa',1,1);

INSERT INTO content_keyword_terms VALUES(1186,593,'en','taxonomy of Russian suicide','taxonomy of russian suicide',1,1);

INSERT INTO content_keyword_terms VALUES(1187,594,'pl','metoda podwójna','metoda podwójna',1,1);

INSERT INTO content_keyword_terms VALUES(1188,594,'en','double method','double method',1,1);

INSERT INTO content_keyword_terms VALUES(1189,595,'pl','cornered animal','cornered animal',1,1);

INSERT INTO content_keyword_terms VALUES(1190,595,'en','cornered animal','cornered animal',1,1);

INSERT INTO content_keyword_terms VALUES(1191,596,'pl','Jałta 3.0','jałta 3.0',1,1);

INSERT INTO content_keyword_terms VALUES(1192,596,'en','Yalta 3.0','yalta 3.0',1,1);

INSERT INTO content_keyword_terms VALUES(1193,597,'pl','aura strachu','aura strachu',1,1);

INSERT INTO content_keyword_terms VALUES(1194,597,'en','aura of fear','aura of fear',1,1);

INSERT INTO content_keyword_terms VALUES(1195,598,'pl','odwrócona metoda naukowa','odwrócona metoda naukowa',1,1);

INSERT INTO content_keyword_terms VALUES(1196,598,'en','reversed scientific method','reversed scientific method',1,1);

INSERT INTO content_keyword_terms VALUES(1197,599,'pl','trzy zagnieżdżone równowagi','trzy zagnieżdżone równowagi',1,1);

INSERT INTO content_keyword_terms VALUES(1198,599,'en','three nested equilibria','three nested equilibria',1,1);

INSERT INTO content_keyword_terms VALUES(1199,600,'pl','autoimmunologia','autoimmunologia',1,1);

INSERT INTO content_keyword_terms VALUES(1200,600,'en','autoimmunity','autoimmunity',1,1);

INSERT INTO content_keyword_terms VALUES(1201,601,'pl','zegar samozniszczenia','zegar samozniszczenia',1,1);

INSERT INTO content_keyword_terms VALUES(1202,601,'en','self-destruct clock','self-destruct clock',1,1);

INSERT INTO content_keyword_terms VALUES(1203,602,'pl','energia jako narzędzie sprawiedliwości','energia jako narzędzie sprawiedliwości',1,1);

INSERT INTO content_keyword_terms VALUES(1204,602,'en','energy as an instrument of justice','energy as an instrument of justice',1,1);

INSERT INTO content_keyword_terms VALUES(1205,306,'pl','pamięć pointer-based','pamięć pointer-based',0,1);

INSERT INTO content_keyword_terms VALUES(1206,105,'pl','fundamentowanie IT','fundamentowanie it',0,1);

INSERT INTO content_keyword_terms VALUES(1207,287,'pl','otwarte loopy','otwarte loopy',0,1);

INSERT INTO content_keyword_terms VALUES(1208,280,'pl','pamięć „złotej rybki”','pamięć „złotej rybki”',0,1);

INSERT INTO content_keyword_terms VALUES(1209,325,'pl','udawanie dorosłego','udawanie dorosłego',0,1);

INSERT INTO content_keyword_terms VALUES(1210,33,'pl','mówienie za mało albo za dużo','mówienie za mało albo za dużo',0,1);

INSERT INTO content_keyword_terms VALUES(1211,421,'pl','schemat-based','schemat-based',0,1);

INSERT INTO content_keyword_terms VALUES(1212,38,'pl','polaroidy babci Genowefy','polaroidy babci genowefy',0,1);

INSERT INTO content_keyword_terms VALUES(1213,147,'pl','pisz pozytywnie','pisz pozytywnie',0,1);

INSERT INTO content_keyword_terms VALUES(1214,14,'pl','arbitr prawdy','arbitr prawdy',0,1);

CREATE INDEX idx_keyword_terms_norm
ON content_keyword_terms(lang, keyword_norm);

