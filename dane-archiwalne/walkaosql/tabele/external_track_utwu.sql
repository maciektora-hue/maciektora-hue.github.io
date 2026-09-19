-- tabela: external_track_utwu
PRAGMA foreign_keys=OFF;

CREATE TABLE IF NOT EXISTS external_track_utwu (
                external_track_pk INTEGER NOT NULL
                    REFERENCES external_track(external_track_pk)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
                utwu_id TEXT NOT NULL
                    REFERENCES middle_end(utwu_id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                PRIMARY KEY (external_track_pk, utwu_id)
            );

INSERT INTO external_track_utwu VALUES(267,'utwu-000174');

INSERT INTO external_track_utwu VALUES(391,'utwu-000083');

INSERT INTO external_track_utwu VALUES(507,'utwu-000051');

INSERT INTO external_track_utwu VALUES(124,'utwu-000062');

INSERT INTO external_track_utwu VALUES(202,'utwu-000074');

INSERT INTO external_track_utwu VALUES(342,'utwu-000555');

INSERT INTO external_track_utwu VALUES(345,'utwu-000561');

INSERT INTO external_track_utwu VALUES(145,'utwu-000111');

INSERT INTO external_track_utwu VALUES(473,'utwu-000093');

INSERT INTO external_track_utwu VALUES(41,'utwu-000026');

INSERT INTO external_track_utwu VALUES(548,'utwu-000326');

INSERT INTO external_track_utwu VALUES(613,'utwu-000069');

INSERT INTO external_track_utwu VALUES(179,'utwu-000132');

INSERT INTO external_track_utwu VALUES(45,'utwu-000356');

INSERT INTO external_track_utwu VALUES(51,'utwu-000123');

INSERT INTO external_track_utwu VALUES(134,'utwu-000220');

INSERT INTO external_track_utwu VALUES(432,'utwu-000288');

INSERT INTO external_track_utwu VALUES(446,'utwu-000019');

INSERT INTO external_track_utwu VALUES(4,'utwu-000422');

INSERT INTO external_track_utwu VALUES(319,'utwu-000196');

INSERT INTO external_track_utwu VALUES(181,'utwu-000055');

INSERT INTO external_track_utwu VALUES(390,'utwu-000120');

INSERT INTO external_track_utwu VALUES(333,'utwu-000056');

INSERT INTO external_track_utwu VALUES(470,'utwu-000129');

INSERT INTO external_track_utwu VALUES(66,'utwu-000209');

INSERT INTO external_track_utwu VALUES(47,'utwu-000122');

INSERT INTO external_track_utwu VALUES(388,'utwu-000253');

INSERT INTO external_track_utwu VALUES(198,'utwu-000256');

INSERT INTO external_track_utwu VALUES(522,'utwu-000535');

INSERT INTO external_track_utwu VALUES(396,'utwu-000077');

INSERT INTO external_track_utwu VALUES(24,'utwu-000102');

INSERT INTO external_track_utwu VALUES(78,'utwu-000130');

INSERT INTO external_track_utwu VALUES(465,'utwu-000106');

INSERT INTO external_track_utwu VALUES(376,'utwu-000117');

INSERT INTO external_track_utwu VALUES(331,'utwu-000042');

INSERT INTO external_track_utwu VALUES(526,'utwu-000082');

INSERT INTO external_track_utwu VALUES(113,'utwu-000514');

INSERT INTO external_track_utwu VALUES(285,'utwu-000126');

INSERT INTO external_track_utwu VALUES(592,'utwu-000127');

INSERT INTO external_track_utwu VALUES(381,'utwu-000706');

INSERT INTO external_track_utwu VALUES(1,'utwu-000335');

INSERT INTO external_track_utwu VALUES(304,'utwu-000116');

INSERT INTO external_track_utwu VALUES(611,'utwu-000121');

INSERT INTO external_track_utwu VALUES(104,'utwu-000180');

INSERT INTO external_track_utwu VALUES(379,'utwu-000124');

INSERT INTO external_track_utwu VALUES(329,'utwu-000110');

INSERT INTO external_track_utwu VALUES(580,'utwu-000115');

INSERT INTO external_track_utwu VALUES(348,'utwu-000023');

INSERT INTO external_track_utwu VALUES(406,'utwu-000045');

INSERT INTO external_track_utwu VALUES(282,'utwu-000178');

INSERT INTO external_track_utwu VALUES(205,'utwu-000541');

INSERT INTO external_track_utwu VALUES(148,'utwu-000869');

INSERT INTO external_track_utwu VALUES(28,'utwu-000070');

INSERT INTO external_track_utwu VALUES(192,'utwu-000025');

INSERT INTO external_track_utwu VALUES(236,'utwu-000131');

INSERT INTO external_track_utwu VALUES(378,'utwu-000057');

INSERT INTO external_track_utwu VALUES(307,'utwu-000482');

INSERT INTO external_track_utwu VALUES(136,'utwu-000442');

INSERT INTO external_track_utwu VALUES(509,'utwu-000071');

INSERT INTO external_track_utwu VALUES(431,'utwu-000096');

INSERT INTO external_track_utwu VALUES(557,'utwu-000113');

INSERT INTO external_track_utwu VALUES(80,'utwu-000787');

INSERT INTO external_track_utwu VALUES(487,'utwu-000339');

INSERT INTO external_track_utwu VALUES(542,'utwu-000274');

INSERT INTO external_track_utwu VALUES(213,'utwu-000038');

INSERT INTO external_track_utwu VALUES(219,'utwu-000098');

INSERT INTO external_track_utwu VALUES(330,'utwu-000355');

INSERT INTO external_track_utwu VALUES(172,'utwu-000086');

INSERT INTO external_track_utwu VALUES(506,'utwu-000128');

INSERT INTO external_track_utwu VALUES(478,'utwu-000828');

INSERT INTO external_track_utwu VALUES(321,'utwu-000846');

INSERT INTO external_track_utwu VALUES(210,'utwu-000269');

INSERT INTO external_track_utwu VALUES(94,'utwu-000568');

INSERT INTO external_track_utwu VALUES(343,'utwu-000041');

INSERT INTO external_track_utwu VALUES(132,'utwu-000663');

INSERT INTO external_track_utwu VALUES(171,'utwu-000133');

INSERT INTO external_track_utwu VALUES(535,'utwu-000231');

INSERT INTO external_track_utwu VALUES(310,'utwu-000118');

INSERT INTO external_track_utwu VALUES(107,'utwu-000312');

INSERT INTO external_track_utwu VALUES(312,'utwu-000807');

INSERT INTO external_track_utwu VALUES(129,'utwu-000443');

INSERT INTO external_track_utwu VALUES(622,'utwu-000448');

INSERT INTO external_track_utwu VALUES(280,'utwu-000472');

INSERT INTO external_track_utwu VALUES(251,'utwu-000488');

INSERT INTO external_track_utwu VALUES(264,'utwu-000198');

INSERT INTO external_track_utwu VALUES(74,'utwu-000085');

INSERT INTO external_track_utwu VALUES(174,'utwu-000081');

INSERT INTO external_track_utwu VALUES(243,'utwu-000146');

INSERT INTO external_track_utwu VALUES(434,'utwu-000446');

INSERT INTO external_track_utwu VALUES(600,'utwu-000455');

INSERT INTO external_track_utwu VALUES(400,'utwu-000509');

INSERT INTO external_track_utwu VALUES(150,'utwu-000172');

INSERT INTO external_track_utwu VALUES(540,'utwu-000826');

INSERT INTO external_track_utwu VALUES(191,'utwu-000024');

INSERT INTO external_track_utwu VALUES(151,'utwu-000108');

INSERT INTO external_track_utwu VALUES(21,'utwu-000090');

INSERT INTO external_track_utwu VALUES(576,'utwu-000059');

INSERT INTO external_track_utwu VALUES(500,'utwu-000140');

INSERT INTO external_track_utwu VALUES(599,'utwu-000419');

INSERT INTO external_track_utwu VALUES(252,'utwu-000043');

INSERT INTO external_track_utwu VALUES(223,'utwu-000065');

INSERT INTO external_track_utwu VALUES(549,'utwu-000032');

INSERT INTO external_track_utwu VALUES(173,'utwu-000052');

INSERT INTO external_track_utwu VALUES(183,'utwu-000079');

INSERT INTO external_track_utwu VALUES(440,'utwu-000512');

INSERT INTO external_track_utwu VALUES(271,'utwu-000114');

INSERT INTO external_track_utwu VALUES(81,'utwu-000190');

INSERT INTO external_track_utwu VALUES(353,'utwu-000456');

INSERT INTO external_track_utwu VALUES(385,'utwu-000084');

INSERT INTO external_track_utwu VALUES(317,'utwu-000078');

INSERT INTO external_track_utwu VALUES(479,'utwu-000214');

INSERT INTO external_track_utwu VALUES(539,'utwu-000040');

INSERT INTO external_track_utwu VALUES(209,'utwu-000227');

INSERT INTO external_track_utwu VALUES(97,'utwu-000047');

INSERT INTO external_track_utwu VALUES(501,'utwu-000112');

INSERT INTO external_track_utwu VALUES(72,'utwu-000234');

INSERT INTO external_track_utwu VALUES(144,'utwu-000119');

INSERT INTO external_track_utwu VALUES(246,'utwu-000575');

INSERT INTO external_track_utwu VALUES(524,'utwu-000492');

INSERT INTO external_track_utwu VALUES(586,'utwu-000307');

INSERT INTO external_track_utwu VALUES(10,'utwu-000290');

INSERT INTO external_track_utwu VALUES(281,'utwu-000805');

INSERT INTO external_track_utwu VALUES(90,'utwu-000806');

INSERT INTO external_track_utwu VALUES(481,'utwu-000013');

INSERT INTO external_track_utwu VALUES(109,'utwu-000150');

INSERT INTO external_track_utwu VALUES(415,'utwu-000012');

INSERT INTO external_track_utwu VALUES(318,'utwu-000810');

INSERT INTO external_track_utwu VALUES(454,'utwu-000808');

INSERT INTO external_track_utwu VALUES(187,'utwu-000629');

INSERT INTO external_track_utwu VALUES(19,'utwu-000240');

INSERT INTO external_track_utwu VALUES(59,'utwu-000001');

INSERT INTO external_track_utwu VALUES(273,'utwu-000606');

INSERT INTO external_track_utwu VALUES(468,'utwu-000534');

INSERT INTO external_track_utwu VALUES(315,'utwu-000004');

INSERT INTO external_track_utwu VALUES(447,'utwu-000790');

INSERT INTO external_track_utwu VALUES(375,'utwu-000733');

INSERT INTO external_track_utwu VALUES(95,'utwu-000503');

INSERT INTO external_track_utwu VALUES(294,'utwu-000296');

INSERT INTO external_track_utwu VALUES(299,'utwu-000343');

INSERT INTO external_track_utwu VALUES(2,'utwu-000008');

INSERT INTO external_track_utwu VALUES(108,'utwu-000757');

INSERT INTO external_track_utwu VALUES(617,'utwu-000817');

INSERT INTO external_track_utwu VALUES(476,'utwu-000755');

INSERT INTO external_track_utwu VALUES(79,'utwu-000007');

INSERT INTO external_track_utwu VALUES(422,'utwu-000854');

INSERT INTO external_track_utwu VALUES(419,'utwu-000809');

INSERT INTO external_track_utwu VALUES(488,'utwu-000605');

INSERT INTO external_track_utwu VALUES(373,'utwu-000610');

INSERT INTO external_track_utwu VALUES(323,'utwu-000737');

INSERT INTO external_track_utwu VALUES(486,'utwu-000014');

INSERT INTO external_track_utwu VALUES(543,'utwu-000738');

INSERT INTO external_track_utwu VALUES(161,'utwu-000739');

INSERT INTO external_track_utwu VALUES(495,'utwu-000740');

INSERT INTO external_track_utwu VALUES(530,'utwu-000741');

INSERT INTO external_track_utwu VALUES(105,'utwu-000607');

INSERT INTO external_track_utwu VALUES(491,'utwu-000609');

INSERT INTO external_track_utwu VALUES(504,'utwu-000745');

INSERT INTO external_track_utwu VALUES(620,'utwu-000743');

INSERT INTO external_track_utwu VALUES(57,'utwu-000744');

INSERT INTO external_track_utwu VALUES(570,'utwu-000302');

INSERT INTO external_track_utwu VALUES(155,'utwu-000746');

INSERT INTO external_track_utwu VALUES(547,'utwu-000750');

INSERT INTO external_track_utwu VALUES(168,'utwu-000747');

INSERT INTO external_track_utwu VALUES(393,'utwu-000748');

INSERT INTO external_track_utwu VALUES(25,'utwu-000749');

INSERT INTO external_track_utwu VALUES(457,'utwu-000751');

INSERT INTO external_track_utwu VALUES(503,'utwu-000614');

INSERT INTO external_track_utwu VALUES(69,'utwu-000752');

INSERT INTO external_track_utwu VALUES(167,'utwu-000753');

INSERT INTO external_track_utwu VALUES(426,'utwu-000754');

INSERT INTO external_track_utwu VALUES(528,'utwu-000009');

INSERT INTO external_track_utwu VALUES(253,'utwu-000611');

INSERT INTO external_track_utwu VALUES(463,'utwu-000756');

INSERT INTO external_track_utwu VALUES(521,'utwu-000758');

INSERT INTO external_track_utwu VALUES(122,'utwu-000760');

INSERT INTO external_track_utwu VALUES(337,'utwu-000759');

INSERT INTO external_track_utwu VALUES(498,'utwu-000761');

INSERT INTO external_track_utwu VALUES(559,'utwu-000762');

INSERT INTO external_track_utwu VALUES(510,'utwu-000608');

INSERT INTO external_track_utwu VALUES(480,'utwu-000617');

INSERT INTO external_track_utwu VALUES(170,'utwu-000763');

INSERT INTO external_track_utwu VALUES(220,'utwu-000765');

INSERT INTO external_track_utwu VALUES(269,'utwu-000768');

INSERT INTO external_track_utwu VALUES(386,'utwu-000764');

INSERT INTO external_track_utwu VALUES(3,'utwu-000766');

INSERT INTO external_track_utwu VALUES(420,'utwu-000767');

INSERT INTO external_track_utwu VALUES(135,'utwu-000729');

INSERT INTO external_track_utwu VALUES(114,'utwu-000622');

INSERT INTO external_track_utwu VALUES(372,'utwu-000769');

INSERT INTO external_track_utwu VALUES(309,'utwu-000770');

INSERT INTO external_track_utwu VALUES(33,'utwu-000390');

INSERT INTO external_track_utwu VALUES(513,'utwu-000771');

INSERT INTO external_track_utwu VALUES(628,'utwu-000772');

INSERT INTO external_track_utwu VALUES(383,'utwu-000773');

INSERT INTO external_track_utwu VALUES(471,'utwu-000774');

INSERT INTO external_track_utwu VALUES(180,'utwu-000775');

INSERT INTO external_track_utwu VALUES(433,'utwu-000776');

INSERT INTO external_track_utwu VALUES(118,'utwu-000786');

INSERT INTO external_track_utwu VALUES(154,'utwu-000785');

INSERT INTO external_track_utwu VALUES(346,'utwu-000777');

INSERT INTO external_track_utwu VALUES(405,'utwu-000784');

INSERT INTO external_track_utwu VALUES(418,'utwu-000783');

INSERT INTO external_track_utwu VALUES(371,'utwu-000788');

INSERT INTO external_track_utwu VALUES(325,'utwu-000789');

INSERT INTO external_track_utwu VALUES(112,'utwu-000791');

INSERT INTO external_track_utwu VALUES(186,'utwu-000792');

INSERT INTO external_track_utwu VALUES(250,'utwu-000793');

INSERT INTO external_track_utwu VALUES(177,'utwu-000628');

INSERT INTO external_track_utwu VALUES(77,'utwu-000778');

INSERT INTO external_track_utwu VALUES(423,'utwu-000794');

INSERT INTO external_track_utwu VALUES(18,'utwu-000795');

INSERT INTO external_track_utwu VALUES(596,'utwu-000796');

INSERT INTO external_track_utwu VALUES(101,'utwu-000782');

INSERT INTO external_track_utwu VALUES(573,'utwu-000797');

INSERT INTO external_track_utwu VALUES(469,'utwu-000798');

INSERT INTO external_track_utwu VALUES(311,'utwu-000799');

INSERT INTO external_track_utwu VALUES(199,'utwu-000800');

INSERT INTO external_track_utwu VALUES(477,'utwu-000781');

INSERT INTO external_track_utwu VALUES(255,'utwu-000780');

INSERT INTO external_track_utwu VALUES(365,'utwu-000801');

INSERT INTO external_track_utwu VALUES(485,'utwu-000626');

INSERT INTO external_track_utwu VALUES(445,'utwu-000802');

INSERT INTO external_track_utwu VALUES(456,'utwu-000803');

INSERT INTO external_track_utwu VALUES(43,'utwu-000804');

INSERT INTO external_track_utwu VALUES(597,'utwu-000779');

INSERT INTO external_track_utwu VALUES(324,'utwu-000153');

INSERT INTO external_track_utwu VALUES(110,'utwu-000016');

INSERT INTO external_track_utwu VALUES(335,'utwu-000037');

INSERT INTO external_track_utwu VALUES(222,'utwu-000029');

INSERT INTO external_track_utwu VALUES(582,'utwu-000028');

INSERT INTO external_track_utwu VALUES(609,'utwu-000020');

INSERT INTO external_track_utwu VALUES(566,'utwu-000039');

INSERT INTO external_track_utwu VALUES(631,'utwu-000669');

INSERT INTO external_track_utwu VALUES(382,'utwu-000021');

INSERT INTO external_track_utwu VALUES(340,'utwu-000031');

INSERT INTO external_track_utwu VALUES(36,'utwu-000046');

INSERT INTO external_track_utwu VALUES(240,'utwu-000015');

INSERT INTO external_track_utwu VALUES(313,'utwu-000018');

INSERT INTO external_track_utwu VALUES(203,'utwu-000017');

INSERT INTO external_track_utwu VALUES(562,'utwu-000027');

INSERT INTO external_track_utwu VALUES(392,'utwu-000709');

INSERT INTO external_track_utwu VALUES(158,'utwu-000022');

INSERT INTO external_track_utwu VALUES(86,'utwu-000035');

INSERT INTO external_track_utwu VALUES(451,'utwu-000034');

INSERT INTO external_track_utwu VALUES(442,'utwu-000033');

INSERT INTO external_track_utwu VALUES(614,'utwu-000710');

INSERT INTO external_track_utwu VALUES(421,'utwu-000036');

INSERT INTO external_track_utwu VALUES(61,'utwu-000050');

INSERT INTO external_track_utwu VALUES(257,'utwu-000053');

INSERT INTO external_track_utwu VALUES(450,'utwu-000049');

INSERT INTO external_track_utwu VALUES(615,'utwu-000711');

INSERT INTO external_track_utwu VALUES(525,'utwu-000048');

INSERT INTO external_track_utwu VALUES(15,'utwu-000054');

INSERT INTO external_track_utwu VALUES(552,'utwu-000712');

INSERT INTO external_track_utwu VALUES(22,'utwu-000063');

INSERT INTO external_track_utwu VALUES(453,'utwu-000061');

INSERT INTO external_track_utwu VALUES(428,'utwu-000058');

INSERT INTO external_track_utwu VALUES(268,'utwu-000713');

INSERT INTO external_track_utwu VALUES(239,'utwu-000010');

INSERT INTO external_track_utwu VALUES(462,'utwu-000003');

INSERT INTO external_track_utwu VALUES(115,'utwu-000064');

INSERT INTO external_track_utwu VALUES(232,'utwu-000714');

INSERT INTO external_track_utwu VALUES(254,'utwu-000005');

INSERT INTO external_track_utwu VALUES(302,'utwu-000715');

INSERT INTO external_track_utwu VALUES(156,'utwu-000002');

INSERT INTO external_track_utwu VALUES(397,'utwu-000044');

INSERT INTO external_track_utwu VALUES(610,'utwu-000716');

INSERT INTO external_track_utwu VALUES(270,'utwu-000717');

INSERT INTO external_track_utwu VALUES(58,'utwu-000060');

INSERT INTO external_track_utwu VALUES(443,'utwu-000718');

INSERT INTO external_track_utwu VALUES(356,'utwu-000073');

INSERT INTO external_track_utwu VALUES(458,'utwu-000720');

INSERT INTO external_track_utwu VALUES(384,'utwu-000719');

INSERT INTO external_track_utwu VALUES(366,'utwu-000722');

INSERT INTO external_track_utwu VALUES(553,'utwu-000721');

INSERT INTO external_track_utwu VALUES(256,'utwu-000723');

INSERT INTO external_track_utwu VALUES(508,'utwu-000724');

INSERT INTO external_track_utwu VALUES(13,'utwu-000725');

INSERT INTO external_track_utwu VALUES(226,'utwu-000006');

INSERT INTO external_track_utwu VALUES(338,'utwu-000726');

INSERT INTO external_track_utwu VALUES(358,'utwu-000066');

INSERT INTO external_track_utwu VALUES(489,'utwu-000727');

INSERT INTO external_track_utwu VALUES(159,'utwu-000728');

INSERT INTO external_track_utwu VALUES(502,'utwu-000736');

INSERT INTO external_track_utwu VALUES(196,'utwu-000735');

INSERT INTO external_track_utwu VALUES(448,'utwu-000734');

INSERT INTO external_track_utwu VALUES(117,'utwu-000732');

INSERT INTO external_track_utwu VALUES(146,'utwu-000731');

INSERT INTO external_track_utwu VALUES(484,'utwu-000730');

INSERT INTO external_track_utwu VALUES(560,'utwu-000125');

INSERT INTO external_track_utwu VALUES(531,'utwu-000088');

INSERT INTO external_track_utwu VALUES(190,'utwu-000094');

INSERT INTO external_track_utwu VALUES(278,'utwu-000089');

INSERT INTO external_track_utwu VALUES(153,'utwu-000091');

INSERT INTO external_track_utwu VALUES(369,'utwu-000109');

INSERT INTO external_track_utwu VALUES(359,'utwu-000095');

INSERT INTO external_track_utwu VALUES(261,'utwu-000103');

INSERT INTO external_track_utwu VALUES(16,'utwu-000030');

INSERT INTO external_track_utwu VALUES(140,'utwu-000097');

INSERT INTO external_track_utwu VALUES(363,'utwu-000068');

INSERT INTO external_track_utwu VALUES(20,'utwu-000080');

INSERT INTO external_track_utwu VALUES(235,'utwu-000104');

INSERT INTO external_track_utwu VALUES(593,'utwu-000107');

INSERT INTO external_track_utwu VALUES(511,'utwu-000092');

INSERT INTO external_track_utwu VALUES(635,'utwu-000076');

INSERT INTO external_track_utwu VALUES(34,'utwu-000067');

INSERT INTO external_track_utwu VALUES(128,'utwu-000099');

INSERT INTO external_track_utwu VALUES(120,'utwu-000105');

INSERT INTO external_track_utwu VALUES(588,'utwu-000101');

INSERT INTO external_track_utwu VALUES(529,'utwu-000563');

INSERT INTO external_track_utwu VALUES(70,'utwu-000075');

INSERT INTO external_track_utwu VALUES(298,'utwu-000100');

INSERT INTO external_track_utwu VALUES(467,'utwu-000072');

INSERT INTO external_track_utwu VALUES(579,'utwu-000707');

INSERT INTO external_track_utwu VALUES(116,'utwu-000139');

INSERT INTO external_track_utwu VALUES(411,'utwu-000708');

INSERT INTO external_track_utwu VALUES(262,'utwu-000228');

INSERT INTO external_track_utwu VALUES(360,'utwu-000236');

INSERT INTO external_track_utwu VALUES(455,'utwu-000212');

INSERT INTO external_track_utwu VALUES(594,'utwu-000211');

INSERT INTO external_track_utwu VALUES(234,'utwu-000235');

INSERT INTO external_track_utwu VALUES(452,'utwu-000216');

INSERT INTO external_track_utwu VALUES(461,'utwu-000238');

INSERT INTO external_track_utwu VALUES(221,'utwu-000205');

INSERT INTO external_track_utwu VALUES(300,'utwu-000217');

INSERT INTO external_track_utwu VALUES(50,'utwu-000213');

INSERT INTO external_track_utwu VALUES(474,'utwu-000225');

INSERT INTO external_track_utwu VALUES(601,'utwu-000230');

INSERT INTO external_track_utwu VALUES(424,'utwu-000226');

INSERT INTO external_track_utwu VALUES(517,'utwu-000232');

INSERT INTO external_track_utwu VALUES(93,'utwu-000229');

INSERT INTO external_track_utwu VALUES(49,'utwu-000210');

INSERT INTO external_track_utwu VALUES(394,'utwu-000218');

INSERT INTO external_track_utwu VALUES(493,'utwu-000672');

INSERT INTO external_track_utwu VALUES(374,'utwu-000400');

INSERT INTO external_track_utwu VALUES(5,'utwu-000204');

INSERT INTO external_track_utwu VALUES(523,'utwu-000224');

INSERT INTO external_track_utwu VALUES(492,'utwu-000222');

INSERT INTO external_track_utwu VALUES(532,'utwu-000189');

INSERT INTO external_track_utwu VALUES(200,'utwu-000673');

INSERT INTO external_track_utwu VALUES(279,'utwu-000221');

INSERT INTO external_track_utwu VALUES(121,'utwu-000674');

INSERT INTO external_track_utwu VALUES(435,'utwu-000145');

INSERT INTO external_track_utwu VALUES(178,'utwu-000254');

INSERT INTO external_track_utwu VALUES(141,'utwu-000675');

INSERT INTO external_track_utwu VALUES(56,'utwu-000677');

INSERT INTO external_track_utwu VALUES(241,'utwu-000199');

INSERT INTO external_track_utwu VALUES(623,'utwu-000676');

INSERT INTO external_track_utwu VALUES(169,'utwu-000678');

INSERT INTO external_track_utwu VALUES(194,'utwu-000679');

INSERT INTO external_track_utwu VALUES(438,'utwu-000680');

INSERT INTO external_track_utwu VALUES(111,'utwu-000681');

INSERT INTO external_track_utwu VALUES(496,'utwu-000291');

INSERT INTO external_track_utwu VALUES(88,'utwu-000328');

INSERT INTO external_track_utwu VALUES(427,'utwu-000327');

INSERT INTO external_track_utwu VALUES(26,'utwu-000682');

INSERT INTO external_track_utwu VALUES(274,'utwu-000239');

INSERT INTO external_track_utwu VALUES(123,'utwu-000683');

INSERT INTO external_track_utwu VALUES(60,'utwu-000684');

INSERT INTO external_track_utwu VALUES(149,'utwu-000685');

INSERT INTO external_track_utwu VALUES(558,'utwu-000147');

INSERT INTO external_track_utwu VALUES(572,'utwu-000686');

INSERT INTO external_track_utwu VALUES(231,'utwu-000687');

INSERT INTO external_track_utwu VALUES(332,'utwu-000688');

INSERT INTO external_track_utwu VALUES(291,'utwu-000247');

INSERT INTO external_track_utwu VALUES(569,'utwu-000245');

INSERT INTO external_track_utwu VALUES(6,'utwu-000689');

INSERT INTO external_track_utwu VALUES(326,'utwu-000690');

INSERT INTO external_track_utwu VALUES(17,'utwu-000197');

INSERT INTO external_track_utwu VALUES(629,'utwu-000691');

INSERT INTO external_track_utwu VALUES(163,'utwu-000208');

INSERT INTO external_track_utwu VALUES(354,'utwu-000248');

INSERT INTO external_track_utwu VALUES(208,'utwu-000692');

INSERT INTO external_track_utwu VALUES(449,'utwu-000693');

INSERT INTO external_track_utwu VALUES(165,'utwu-000694');

INSERT INTO external_track_utwu VALUES(351,'utwu-000695');

INSERT INTO external_track_utwu VALUES(293,'utwu-000696');

INSERT INTO external_track_utwu VALUES(377,'utwu-000697');

INSERT INTO external_track_utwu VALUES(147,'utwu-000698');

INSERT INTO external_track_utwu VALUES(409,'utwu-000246');

INSERT INTO external_track_utwu VALUES(106,'utwu-000570');

INSERT INTO external_track_utwu VALUES(204,'utwu-000699');

INSERT INTO external_track_utwu VALUES(533,'utwu-000701');

INSERT INTO external_track_utwu VALUES(272,'utwu-000333');

INSERT INTO external_track_utwu VALUES(550,'utwu-000702');

INSERT INTO external_track_utwu VALUES(621,'utwu-000087');

INSERT INTO external_track_utwu VALUES(425,'utwu-000346');

INSERT INTO external_track_utwu VALUES(556,'utwu-000324');

INSERT INTO external_track_utwu VALUES(355,'utwu-000345');

INSERT INTO external_track_utwu VALUES(62,'utwu-000347');

INSERT INTO external_track_utwu VALUES(27,'utwu-000351');

INSERT INTO external_track_utwu VALUES(185,'utwu-000323');

INSERT INTO external_track_utwu VALUES(632,'utwu-000359');

INSERT INTO external_track_utwu VALUES(612,'utwu-000349');

INSERT INTO external_track_utwu VALUES(207,'utwu-000354');

INSERT INTO external_track_utwu VALUES(227,'utwu-000334');

INSERT INTO external_track_utwu VALUES(368,'utwu-000350');

INSERT INTO external_track_utwu VALUES(244,'utwu-000340');

INSERT INTO external_track_utwu VALUES(537,'utwu-000353');

INSERT INTO external_track_utwu VALUES(228,'utwu-000338');

INSERT INTO external_track_utwu VALUES(103,'utwu-000306');

INSERT INTO external_track_utwu VALUES(604,'utwu-000309');

INSERT INTO external_track_utwu VALUES(316,'utwu-000317');

INSERT INTO external_track_utwu VALUES(188,'utwu-000360');

INSERT INTO external_track_utwu VALUES(536,'utwu-000267');

INSERT INTO external_track_utwu VALUES(551,'utwu-000348');

INSERT INTO external_track_utwu VALUES(590,'utwu-000332');

INSERT INTO external_track_utwu VALUES(595,'utwu-000358');

INSERT INTO external_track_utwu VALUES(225,'utwu-000407');

INSERT INTO external_track_utwu VALUES(23,'utwu-000432');

INSERT INTO external_track_utwu VALUES(505,'utwu-000380');

INSERT INTO external_track_utwu VALUES(215,'utwu-000329');

INSERT INTO external_track_utwu VALUES(619,'utwu-000318');

INSERT INTO external_track_utwu VALUES(483,'utwu-000272');

INSERT INTO external_track_utwu VALUES(618,'utwu-000439');

INSERT INTO external_track_utwu VALUES(357,'utwu-000703');

INSERT INTO external_track_utwu VALUES(217,'utwu-000310');

INSERT INTO external_track_utwu VALUES(362,'utwu-000285');

INSERT INTO external_track_utwu VALUES(295,'utwu-000320');

INSERT INTO external_track_utwu VALUES(37,'utwu-000325');

INSERT INTO external_track_utwu VALUES(460,'utwu-000352');

INSERT INTO external_track_utwu VALUES(341,'utwu-000450');

INSERT INTO external_track_utwu VALUES(89,'utwu-000704');

INSERT INTO external_track_utwu VALUES(157,'utwu-000321');

INSERT INTO external_track_utwu VALUES(430,'utwu-000363');

INSERT INTO external_track_utwu VALUES(361,'utwu-000336');

INSERT INTO external_track_utwu VALUES(92,'utwu-000255');

INSERT INTO external_track_utwu VALUES(625,'utwu-000279');

INSERT INTO external_track_utwu VALUES(71,'utwu-000311');

INSERT INTO external_track_utwu VALUES(119,'utwu-000421');

INSERT INTO external_track_utwu VALUES(567,'utwu-000377');

INSERT INTO external_track_utwu VALUES(494,'utwu-000437');

INSERT INTO external_track_utwu VALUES(305,'utwu-000433');

INSERT INTO external_track_utwu VALUES(245,'utwu-000478');

INSERT INTO external_track_utwu VALUES(575,'utwu-000408');

INSERT INTO external_track_utwu VALUES(98,'utwu-000705');

INSERT INTO external_track_utwu VALUES(464,'utwu-000266');

INSERT INTO external_track_utwu VALUES(230,'utwu-000305');

INSERT INTO external_track_utwu VALUES(193,'utwu-000364');

INSERT INTO external_track_utwu VALUES(336,'utwu-000304');

INSERT INTO external_track_utwu VALUES(11,'utwu-000517');

INSERT INTO external_track_utwu VALUES(561,'utwu-000545');

INSERT INTO external_track_utwu VALUES(32,'utwu-000559');

INSERT INTO external_track_utwu VALUES(224,'utwu-000564');

INSERT INTO external_track_utwu VALUES(68,'utwu-000527');

INSERT INTO external_track_utwu VALUES(367,'utwu-000464');

INSERT INTO external_track_utwu VALUES(633,'utwu-000522');

INSERT INTO external_track_utwu VALUES(437,'utwu-000465');

INSERT INTO external_track_utwu VALUES(516,'utwu-000518');

INSERT INTO external_track_utwu VALUES(554,'utwu-000477');

INSERT INTO external_track_utwu VALUES(563,'utwu-000567');

INSERT INTO external_track_utwu VALUES(53,'utwu-000489');

INSERT INTO external_track_utwu VALUES(297,'utwu-000467');

INSERT INTO external_track_utwu VALUES(459,'utwu-000537');

INSERT INTO external_track_utwu VALUES(214,'utwu-000560');

INSERT INTO external_track_utwu VALUES(578,'utwu-000569');

INSERT INTO external_track_utwu VALUES(308,'utwu-000454');

INSERT INTO external_track_utwu VALUES(328,'utwu-000458');

INSERT INTO external_track_utwu VALUES(131,'utwu-000566');

INSERT INTO external_track_utwu VALUES(349,'utwu-000562');

INSERT INTO external_track_utwu VALUES(581,'utwu-000487');

INSERT INTO external_track_utwu VALUES(182,'utwu-000485');

INSERT INTO external_track_utwu VALUES(518,'utwu-000542');

INSERT INTO external_track_utwu VALUES(538,'utwu-000479');

INSERT INTO external_track_utwu VALUES(568,'utwu-000470');

INSERT INTO external_track_utwu VALUES(334,'utwu-000425');

INSERT INTO external_track_utwu VALUES(189,'utwu-000544');

INSERT INTO external_track_utwu VALUES(387,'utwu-000475');

INSERT INTO external_track_utwu VALUES(7,'utwu-000484');

INSERT INTO external_track_utwu VALUES(414,'utwu-000552');

INSERT INTO external_track_utwu VALUES(82,'utwu-000521');

INSERT INTO external_track_utwu VALUES(259,'utwu-000530');

INSERT INTO external_track_utwu VALUES(63,'utwu-000548');

INSERT INTO external_track_utwu VALUES(143,'utwu-000526');

INSERT INTO external_track_utwu VALUES(534,'utwu-000453');

INSERT INTO external_track_utwu VALUES(606,'utwu-000550');

INSERT INTO external_track_utwu VALUES(284,'utwu-000468');

INSERT INTO external_track_utwu VALUES(389,'utwu-000430');

INSERT INTO external_track_utwu VALUES(364,'utwu-000528');

INSERT INTO external_track_utwu VALUES(303,'utwu-000449');

INSERT INTO external_track_utwu VALUES(265,'utwu-000476');

INSERT INTO external_track_utwu VALUES(160,'utwu-000524');

INSERT INTO external_track_utwu VALUES(499,'utwu-000480');

INSERT INTO external_track_utwu VALUES(520,'utwu-000525');

INSERT INTO external_track_utwu VALUES(130,'utwu-000513');

INSERT INTO external_track_utwu VALUES(466,'utwu-000543');

INSERT INTO external_track_utwu VALUES(84,'utwu-000540');

INSERT INTO external_track_utwu VALUES(102,'utwu-000435');

INSERT INTO external_track_utwu VALUES(603,'utwu-000551');

INSERT INTO external_track_utwu VALUES(96,'utwu-000558');

INSERT INTO external_track_utwu VALUES(370,'utwu-000511');

INSERT INTO external_track_utwu VALUES(142,'utwu-000451');

INSERT INTO external_track_utwu VALUES(242,'utwu-000515');

INSERT INTO external_track_utwu VALUES(545,'utwu-000700');

INSERT INTO external_track_utwu VALUES(439,'utwu-000486');

INSERT INTO external_track_utwu VALUES(395,'utwu-000549');

INSERT INTO external_track_utwu VALUES(42,'utwu-000436');

INSERT INTO external_track_utwu VALUES(585,'utwu-000505');

INSERT INTO external_track_utwu VALUES(583,'utwu-000529');

INSERT INTO external_track_utwu VALUES(206,'utwu-000532');

INSERT INTO external_track_utwu VALUES(46,'utwu-000557');

INSERT INTO external_track_utwu VALUES(233,'utwu-000536');

INSERT INTO external_track_utwu VALUES(490,'utwu-000504');

INSERT INTO external_track_utwu VALUES(544,'utwu-000533');

INSERT INTO external_track_utwu VALUES(12,'utwu-000538');

INSERT INTO external_track_utwu VALUES(176,'utwu-000462');

INSERT INTO external_track_utwu VALUES(39,'utwu-000539');

INSERT INTO external_track_utwu VALUES(289,'utwu-000452');

INSERT INTO external_track_utwu VALUES(417,'utwu-000466');

INSERT INTO external_track_utwu VALUES(555,'utwu-000520');

INSERT INTO external_track_utwu VALUES(436,'utwu-000473');

INSERT INTO external_track_utwu VALUES(602,'utwu-000519');

INSERT INTO external_track_utwu VALUES(137,'utwu-000495');

INSERT INTO external_track_utwu VALUES(277,'utwu-000501');

INSERT INTO external_track_utwu VALUES(497,'utwu-000491');

INSERT INTO external_track_utwu VALUES(608,'utwu-000490');

INSERT INTO external_track_utwu VALUES(624,'utwu-000565');

INSERT INTO external_track_utwu VALUES(247,'utwu-000658');

INSERT INTO external_track_utwu VALUES(408,'utwu-000829');

INSERT INTO external_track_utwu VALUES(201,'utwu-000661');

INSERT INTO external_track_utwu VALUES(48,'utwu-000588');

INSERT INTO external_track_utwu VALUES(429,'utwu-000576');

INSERT INTO external_track_utwu VALUES(249,'utwu-000593');

INSERT INTO external_track_utwu VALUES(73,'utwu-000573');

INSERT INTO external_track_utwu VALUES(133,'utwu-000598');

INSERT INTO external_track_utwu VALUES(482,'utwu-000592');

INSERT INTO external_track_utwu VALUES(630,'utwu-000668');

INSERT INTO external_track_utwu VALUES(402,'utwu-000827');

INSERT INTO external_track_utwu VALUES(54,'utwu-000585');

INSERT INTO external_track_utwu VALUES(636,'utwu-000600');

INSERT INTO external_track_utwu VALUES(211,'utwu-000830');

INSERT INTO external_track_utwu VALUES(598,'utwu-000665');

INSERT INTO external_track_utwu VALUES(515,'utwu-000660');

INSERT INTO external_track_utwu VALUES(574,'utwu-000662');

INSERT INTO external_track_utwu VALUES(40,'utwu-000848');

INSERT INTO external_track_utwu VALUES(83,'utwu-000398');

INSERT INTO external_track_utwu VALUES(175,'utwu-000506');

INSERT INTO external_track_utwu VALUES(344,'utwu-000597');

INSERT INTO external_track_utwu VALUES(287,'utwu-000839');

INSERT INTO external_track_utwu VALUES(347,'utwu-000403');

INSERT INTO external_track_utwu VALUES(626,'utwu-000635');

INSERT INTO external_track_utwu VALUES(197,'utwu-000667');

INSERT INTO external_track_utwu VALUES(444,'utwu-000280');

INSERT INTO external_track_utwu VALUES(640,'utwu-000938');

INSERT INTO external_track_utwu VALUES(641,'utwu-000937');

INSERT INTO external_track_utwu VALUES(642,'utwu-000936');

INSERT INTO external_track_utwu VALUES(643,'utwu-000935');

INSERT INTO external_track_utwu VALUES(644,'utwu-000934');

INSERT INTO external_track_utwu VALUES(645,'utwu-000933');

INSERT INTO external_track_utwu VALUES(646,'utwu-000932');

INSERT INTO external_track_utwu VALUES(647,'utwu-000931');

INSERT INTO external_track_utwu VALUES(648,'utwu-000930');

INSERT INTO external_track_utwu VALUES(649,'utwu-000929');

INSERT INTO external_track_utwu VALUES(650,'utwu-000928');

INSERT INTO external_track_utwu VALUES(651,'utwu-000927');

INSERT INTO external_track_utwu VALUES(652,'utwu-000926');

INSERT INTO external_track_utwu VALUES(653,'utwu-000925');

INSERT INTO external_track_utwu VALUES(654,'utwu-000924');

INSERT INTO external_track_utwu VALUES(655,'utwu-000923');

INSERT INTO external_track_utwu VALUES(656,'utwu-000922');

INSERT INTO external_track_utwu VALUES(657,'utwu-000921');

INSERT INTO external_track_utwu VALUES(658,'utwu-000920');

INSERT INTO external_track_utwu VALUES(659,'utwu-000919');

INSERT INTO external_track_utwu VALUES(660,'utwu-000918');

INSERT INTO external_track_utwu VALUES(661,'utwu-000917');

INSERT INTO external_track_utwu VALUES(662,'utwu-000916');

INSERT INTO external_track_utwu VALUES(663,'utwu-000915');

INSERT INTO external_track_utwu VALUES(664,'utwu-000914');

INSERT INTO external_track_utwu VALUES(665,'utwu-000913');

INSERT INTO external_track_utwu VALUES(666,'utwu-000912');

INSERT INTO external_track_utwu VALUES(667,'utwu-000911');

INSERT INTO external_track_utwu VALUES(668,'utwu-000910');

INSERT INTO external_track_utwu VALUES(669,'utwu-000909');

INSERT INTO external_track_utwu VALUES(670,'utwu-000908');

INSERT INTO external_track_utwu VALUES(671,'utwu-000907');

INSERT INTO external_track_utwu VALUES(672,'utwu-000906');

INSERT INTO external_track_utwu VALUES(673,'utwu-000905');

INSERT INTO external_track_utwu VALUES(674,'utwu-000904');

INSERT INTO external_track_utwu VALUES(675,'utwu-000903');

INSERT INTO external_track_utwu VALUES(676,'utwu-000902');

INSERT INTO external_track_utwu VALUES(677,'utwu-000901');

INSERT INTO external_track_utwu VALUES(678,'utwu-000900');

INSERT INTO external_track_utwu VALUES(679,'utwu-000899');

INSERT INTO external_track_utwu VALUES(680,'utwu-000898');

INSERT INTO external_track_utwu VALUES(681,'utwu-000897');

INSERT INTO external_track_utwu VALUES(682,'utwu-000896');

INSERT INTO external_track_utwu VALUES(683,'utwu-000895');

INSERT INTO external_track_utwu VALUES(684,'utwu-000894');

INSERT INTO external_track_utwu VALUES(685,'utwu-000893');

INSERT INTO external_track_utwu VALUES(686,'utwu-000892');

INSERT INTO external_track_utwu VALUES(687,'utwu-000891');

INSERT INTO external_track_utwu VALUES(688,'utwu-000890');

INSERT INTO external_track_utwu VALUES(689,'utwu-000889');

INSERT INTO external_track_utwu VALUES(690,'utwu-000888');

INSERT INTO external_track_utwu VALUES(691,'utwu-000887');

INSERT INTO external_track_utwu VALUES(692,'utwu-000886');

INSERT INTO external_track_utwu VALUES(693,'utwu-000885');

INSERT INTO external_track_utwu VALUES(694,'utwu-000884');

INSERT INTO external_track_utwu VALUES(695,'utwu-000883');

INSERT INTO external_track_utwu VALUES(696,'utwu-000882');

INSERT INTO external_track_utwu VALUES(697,'utwu-000881');

INSERT INTO external_track_utwu VALUES(698,'utwu-000880');

INSERT INTO external_track_utwu VALUES(699,'utwu-000879');

INSERT INTO external_track_utwu VALUES(700,'utwu-000878');

INSERT INTO external_track_utwu VALUES(701,'utwu-000877');

INSERT INTO external_track_utwu VALUES(702,'utwu-000876');

INSERT INTO external_track_utwu VALUES(703,'utwu-000875');

INSERT INTO external_track_utwu VALUES(704,'utwu-000874');

INSERT INTO external_track_utwu VALUES(705,'utwu-000873');

INSERT INTO external_track_utwu VALUES(706,'utwu-000872');

INSERT INTO external_track_utwu VALUES(707,'utwu-000871');

INSERT INTO external_track_utwu VALUES(708,'utwu-000870');

INSERT INTO external_track_utwu VALUES(709,'utwu-000868');

INSERT INTO external_track_utwu VALUES(710,'utwu-000867');

INSERT INTO external_track_utwu VALUES(711,'utwu-000866');

INSERT INTO external_track_utwu VALUES(712,'utwu-000865');

INSERT INTO external_track_utwu VALUES(713,'utwu-000864');

INSERT INTO external_track_utwu VALUES(714,'utwu-000863');

INSERT INTO external_track_utwu VALUES(715,'utwu-000862');

INSERT INTO external_track_utwu VALUES(716,'utwu-000861');

INSERT INTO external_track_utwu VALUES(717,'utwu-000860');

INSERT INTO external_track_utwu VALUES(718,'utwu-000859');

INSERT INTO external_track_utwu VALUES(719,'utwu-000858');

INSERT INTO external_track_utwu VALUES(720,'utwu-000857');

INSERT INTO external_track_utwu VALUES(721,'utwu-000856');

INSERT INTO external_track_utwu VALUES(722,'utwu-000855');

INSERT INTO external_track_utwu VALUES(723,'utwu-000853');

INSERT INTO external_track_utwu VALUES(724,'utwu-000852');

INSERT INTO external_track_utwu VALUES(725,'utwu-000851');

INSERT INTO external_track_utwu VALUES(726,'utwu-000850');

INSERT INTO external_track_utwu VALUES(727,'utwu-000849');

INSERT INTO external_track_utwu VALUES(728,'utwu-000847');

INSERT INTO external_track_utwu VALUES(729,'utwu-000845');

INSERT INTO external_track_utwu VALUES(730,'utwu-000844');

INSERT INTO external_track_utwu VALUES(731,'utwu-000843');

INSERT INTO external_track_utwu VALUES(732,'utwu-000842');

INSERT INTO external_track_utwu VALUES(733,'utwu-000841');

INSERT INTO external_track_utwu VALUES(734,'utwu-000840');

INSERT INTO external_track_utwu VALUES(735,'utwu-000838');

INSERT INTO external_track_utwu VALUES(736,'utwu-000837');

INSERT INTO external_track_utwu VALUES(737,'utwu-000836');

INSERT INTO external_track_utwu VALUES(738,'utwu-000835');

INSERT INTO external_track_utwu VALUES(739,'utwu-000834');

INSERT INTO external_track_utwu VALUES(740,'utwu-000833');

INSERT INTO external_track_utwu VALUES(741,'utwu-000832');

INSERT INTO external_track_utwu VALUES(742,'utwu-000831');

INSERT INTO external_track_utwu VALUES(743,'utwu-000825');

INSERT INTO external_track_utwu VALUES(744,'utwu-000824');

INSERT INTO external_track_utwu VALUES(745,'utwu-000823');

INSERT INTO external_track_utwu VALUES(746,'utwu-000822');

INSERT INTO external_track_utwu VALUES(747,'utwu-000821');

INSERT INTO external_track_utwu VALUES(748,'utwu-000820');

INSERT INTO external_track_utwu VALUES(749,'utwu-000819');

INSERT INTO external_track_utwu VALUES(750,'utwu-000818');

INSERT INTO external_track_utwu VALUES(751,'utwu-000816');

INSERT INTO external_track_utwu VALUES(752,'utwu-000815');

INSERT INTO external_track_utwu VALUES(753,'utwu-000814');

INSERT INTO external_track_utwu VALUES(754,'utwu-000813');

INSERT INTO external_track_utwu VALUES(755,'utwu-000812');

INSERT INTO external_track_utwu VALUES(756,'utwu-000811');

INSERT INTO external_track_utwu VALUES(757,'utwu-000671');

INSERT INTO external_track_utwu VALUES(758,'utwu-000670');

INSERT INTO external_track_utwu VALUES(759,'utwu-000666');

INSERT INTO external_track_utwu VALUES(760,'utwu-000664');

INSERT INTO external_track_utwu VALUES(761,'utwu-000659');

INSERT INTO external_track_utwu VALUES(762,'utwu-000657');

INSERT INTO external_track_utwu VALUES(763,'utwu-000656');

INSERT INTO external_track_utwu VALUES(764,'utwu-000655');

INSERT INTO external_track_utwu VALUES(765,'utwu-000654');

INSERT INTO external_track_utwu VALUES(766,'utwu-000653');

INSERT INTO external_track_utwu VALUES(767,'utwu-000652');

INSERT INTO external_track_utwu VALUES(768,'utwu-000651');

INSERT INTO external_track_utwu VALUES(769,'utwu-000650');

INSERT INTO external_track_utwu VALUES(770,'utwu-000649');

INSERT INTO external_track_utwu VALUES(771,'utwu-000648');

INSERT INTO external_track_utwu VALUES(772,'utwu-000647');

INSERT INTO external_track_utwu VALUES(773,'utwu-000646');

INSERT INTO external_track_utwu VALUES(774,'utwu-000645');

INSERT INTO external_track_utwu VALUES(775,'utwu-000644');

INSERT INTO external_track_utwu VALUES(776,'utwu-000643');

INSERT INTO external_track_utwu VALUES(777,'utwu-000642');

INSERT INTO external_track_utwu VALUES(778,'utwu-000641');

INSERT INTO external_track_utwu VALUES(779,'utwu-000640');

INSERT INTO external_track_utwu VALUES(780,'utwu-000639');

INSERT INTO external_track_utwu VALUES(781,'utwu-000638');

INSERT INTO external_track_utwu VALUES(782,'utwu-000637');

INSERT INTO external_track_utwu VALUES(783,'utwu-000636');

INSERT INTO external_track_utwu VALUES(784,'utwu-000634');

INSERT INTO external_track_utwu VALUES(785,'utwu-000633');

INSERT INTO external_track_utwu VALUES(786,'utwu-000632');

INSERT INTO external_track_utwu VALUES(787,'utwu-000631');

INSERT INTO external_track_utwu VALUES(788,'utwu-000630');

INSERT INTO external_track_utwu VALUES(789,'utwu-000627');

INSERT INTO external_track_utwu VALUES(790,'utwu-000625');

INSERT INTO external_track_utwu VALUES(791,'utwu-000624');

INSERT INTO external_track_utwu VALUES(792,'utwu-000623');

INSERT INTO external_track_utwu VALUES(793,'utwu-000621');

INSERT INTO external_track_utwu VALUES(794,'utwu-000620');

INSERT INTO external_track_utwu VALUES(795,'utwu-000619');

INSERT INTO external_track_utwu VALUES(796,'utwu-000618');

INSERT INTO external_track_utwu VALUES(797,'utwu-000616');

INSERT INTO external_track_utwu VALUES(798,'utwu-000615');

INSERT INTO external_track_utwu VALUES(799,'utwu-000613');

INSERT INTO external_track_utwu VALUES(800,'utwu-000612');

INSERT INTO external_track_utwu VALUES(801,'utwu-000604');

INSERT INTO external_track_utwu VALUES(802,'utwu-000603');

INSERT INTO external_track_utwu VALUES(803,'utwu-000602');

INSERT INTO external_track_utwu VALUES(804,'utwu-000601');

INSERT INTO external_track_utwu VALUES(805,'utwu-000599');

INSERT INTO external_track_utwu VALUES(806,'utwu-000596');

INSERT INTO external_track_utwu VALUES(807,'utwu-000595');

INSERT INTO external_track_utwu VALUES(808,'utwu-000594');

INSERT INTO external_track_utwu VALUES(809,'utwu-000591');

INSERT INTO external_track_utwu VALUES(810,'utwu-000590');

INSERT INTO external_track_utwu VALUES(811,'utwu-000589');

INSERT INTO external_track_utwu VALUES(812,'utwu-000587');

INSERT INTO external_track_utwu VALUES(813,'utwu-000586');

INSERT INTO external_track_utwu VALUES(814,'utwu-000584');

INSERT INTO external_track_utwu VALUES(815,'utwu-000583');

INSERT INTO external_track_utwu VALUES(816,'utwu-000582');

INSERT INTO external_track_utwu VALUES(817,'utwu-000581');

INSERT INTO external_track_utwu VALUES(818,'utwu-000580');

INSERT INTO external_track_utwu VALUES(819,'utwu-000579');

INSERT INTO external_track_utwu VALUES(820,'utwu-000578');

INSERT INTO external_track_utwu VALUES(821,'utwu-000577');

INSERT INTO external_track_utwu VALUES(822,'utwu-000574');

INSERT INTO external_track_utwu VALUES(823,'utwu-000572');

INSERT INTO external_track_utwu VALUES(824,'utwu-000571');

INSERT INTO external_track_utwu VALUES(825,'utwu-000556');

INSERT INTO external_track_utwu VALUES(826,'utwu-000554');

INSERT INTO external_track_utwu VALUES(827,'utwu-000553');

INSERT INTO external_track_utwu VALUES(828,'utwu-000547');

INSERT INTO external_track_utwu VALUES(829,'utwu-000546');

INSERT INTO external_track_utwu VALUES(830,'utwu-000531');

INSERT INTO external_track_utwu VALUES(831,'utwu-000523');

INSERT INTO external_track_utwu VALUES(832,'utwu-000516');

INSERT INTO external_track_utwu VALUES(833,'utwu-000510');

INSERT INTO external_track_utwu VALUES(834,'utwu-000508');

INSERT INTO external_track_utwu VALUES(835,'utwu-000507');

INSERT INTO external_track_utwu VALUES(836,'utwu-000502');

INSERT INTO external_track_utwu VALUES(837,'utwu-000500');

INSERT INTO external_track_utwu VALUES(838,'utwu-000499');

INSERT INTO external_track_utwu VALUES(839,'utwu-000498');

INSERT INTO external_track_utwu VALUES(840,'utwu-000497');

INSERT INTO external_track_utwu VALUES(841,'utwu-000496');

INSERT INTO external_track_utwu VALUES(842,'utwu-000494');

INSERT INTO external_track_utwu VALUES(843,'utwu-000493');

INSERT INTO external_track_utwu VALUES(844,'utwu-000483');

INSERT INTO external_track_utwu VALUES(845,'utwu-000481');

INSERT INTO external_track_utwu VALUES(846,'utwu-000474');

INSERT INTO external_track_utwu VALUES(847,'utwu-000471');

INSERT INTO external_track_utwu VALUES(848,'utwu-000469');

INSERT INTO external_track_utwu VALUES(849,'utwu-000463');

INSERT INTO external_track_utwu VALUES(850,'utwu-000461');

INSERT INTO external_track_utwu VALUES(851,'utwu-000460');

INSERT INTO external_track_utwu VALUES(852,'utwu-000459');

INSERT INTO external_track_utwu VALUES(853,'utwu-000457');

INSERT INTO external_track_utwu VALUES(854,'utwu-000447');

INSERT INTO external_track_utwu VALUES(855,'utwu-000445');

INSERT INTO external_track_utwu VALUES(856,'utwu-000444');

INSERT INTO external_track_utwu VALUES(857,'utwu-000441');

INSERT INTO external_track_utwu VALUES(858,'utwu-000440');

INSERT INTO external_track_utwu VALUES(859,'utwu-000438');

INSERT INTO external_track_utwu VALUES(860,'utwu-000434');

INSERT INTO external_track_utwu VALUES(861,'utwu-000431');

INSERT INTO external_track_utwu VALUES(862,'utwu-000429');

INSERT INTO external_track_utwu VALUES(863,'utwu-000428');

INSERT INTO external_track_utwu VALUES(864,'utwu-000427');

INSERT INTO external_track_utwu VALUES(865,'utwu-000426');

INSERT INTO external_track_utwu VALUES(866,'utwu-000424');

INSERT INTO external_track_utwu VALUES(867,'utwu-000423');

INSERT INTO external_track_utwu VALUES(868,'utwu-000420');

INSERT INTO external_track_utwu VALUES(869,'utwu-000418');

INSERT INTO external_track_utwu VALUES(870,'utwu-000417');

INSERT INTO external_track_utwu VALUES(871,'utwu-000416');

INSERT INTO external_track_utwu VALUES(872,'utwu-000415');

INSERT INTO external_track_utwu VALUES(873,'utwu-000414');

INSERT INTO external_track_utwu VALUES(874,'utwu-000413');

INSERT INTO external_track_utwu VALUES(875,'utwu-000412');

INSERT INTO external_track_utwu VALUES(876,'utwu-000411');

INSERT INTO external_track_utwu VALUES(877,'utwu-000410');

INSERT INTO external_track_utwu VALUES(878,'utwu-000409');

INSERT INTO external_track_utwu VALUES(879,'utwu-000406');

INSERT INTO external_track_utwu VALUES(880,'utwu-000405');

INSERT INTO external_track_utwu VALUES(881,'utwu-000404');

INSERT INTO external_track_utwu VALUES(882,'utwu-000402');

INSERT INTO external_track_utwu VALUES(883,'utwu-000401');

INSERT INTO external_track_utwu VALUES(884,'utwu-000399');

INSERT INTO external_track_utwu VALUES(885,'utwu-000397');

INSERT INTO external_track_utwu VALUES(886,'utwu-000396');

INSERT INTO external_track_utwu VALUES(887,'utwu-000395');

INSERT INTO external_track_utwu VALUES(888,'utwu-000394');

INSERT INTO external_track_utwu VALUES(889,'utwu-000393');

INSERT INTO external_track_utwu VALUES(890,'utwu-000392');

INSERT INTO external_track_utwu VALUES(891,'utwu-000391');

INSERT INTO external_track_utwu VALUES(892,'utwu-000389');

INSERT INTO external_track_utwu VALUES(893,'utwu-000388');

INSERT INTO external_track_utwu VALUES(894,'utwu-000387');

INSERT INTO external_track_utwu VALUES(895,'utwu-000386');

INSERT INTO external_track_utwu VALUES(896,'utwu-000385');

INSERT INTO external_track_utwu VALUES(897,'utwu-000384');

INSERT INTO external_track_utwu VALUES(898,'utwu-000383');

INSERT INTO external_track_utwu VALUES(899,'utwu-000382');

INSERT INTO external_track_utwu VALUES(900,'utwu-000381');

INSERT INTO external_track_utwu VALUES(901,'utwu-000379');

INSERT INTO external_track_utwu VALUES(902,'utwu-000378');

INSERT INTO external_track_utwu VALUES(903,'utwu-000376');

INSERT INTO external_track_utwu VALUES(904,'utwu-000375');

INSERT INTO external_track_utwu VALUES(905,'utwu-000374');

INSERT INTO external_track_utwu VALUES(906,'utwu-000373');

INSERT INTO external_track_utwu VALUES(907,'utwu-000372');

INSERT INTO external_track_utwu VALUES(908,'utwu-000371');

INSERT INTO external_track_utwu VALUES(909,'utwu-000370');

INSERT INTO external_track_utwu VALUES(910,'utwu-000369');

INSERT INTO external_track_utwu VALUES(911,'utwu-000368');

INSERT INTO external_track_utwu VALUES(912,'utwu-000367');

INSERT INTO external_track_utwu VALUES(913,'utwu-000366');

INSERT INTO external_track_utwu VALUES(914,'utwu-000365');

INSERT INTO external_track_utwu VALUES(915,'utwu-000362');

INSERT INTO external_track_utwu VALUES(916,'utwu-000361');

INSERT INTO external_track_utwu VALUES(917,'utwu-000357');

INSERT INTO external_track_utwu VALUES(918,'utwu-000344');

INSERT INTO external_track_utwu VALUES(919,'utwu-000342');

INSERT INTO external_track_utwu VALUES(920,'utwu-000341');

INSERT INTO external_track_utwu VALUES(921,'utwu-000337');

INSERT INTO external_track_utwu VALUES(922,'utwu-000331');

INSERT INTO external_track_utwu VALUES(923,'utwu-000330');

INSERT INTO external_track_utwu VALUES(924,'utwu-000322');

INSERT INTO external_track_utwu VALUES(925,'utwu-000319');

INSERT INTO external_track_utwu VALUES(926,'utwu-000316');

INSERT INTO external_track_utwu VALUES(927,'utwu-000315');

INSERT INTO external_track_utwu VALUES(928,'utwu-000314');

INSERT INTO external_track_utwu VALUES(929,'utwu-000313');

INSERT INTO external_track_utwu VALUES(930,'utwu-000308');

INSERT INTO external_track_utwu VALUES(931,'utwu-000303');

INSERT INTO external_track_utwu VALUES(932,'utwu-000301');

INSERT INTO external_track_utwu VALUES(933,'utwu-000300');

INSERT INTO external_track_utwu VALUES(934,'utwu-000299');

INSERT INTO external_track_utwu VALUES(935,'utwu-000298');

INSERT INTO external_track_utwu VALUES(936,'utwu-000297');

INSERT INTO external_track_utwu VALUES(937,'utwu-000295');

INSERT INTO external_track_utwu VALUES(938,'utwu-000294');

INSERT INTO external_track_utwu VALUES(939,'utwu-000293');

INSERT INTO external_track_utwu VALUES(940,'utwu-000292');

INSERT INTO external_track_utwu VALUES(941,'utwu-000289');

INSERT INTO external_track_utwu VALUES(942,'utwu-000287');

INSERT INTO external_track_utwu VALUES(943,'utwu-000286');

INSERT INTO external_track_utwu VALUES(944,'utwu-000284');

INSERT INTO external_track_utwu VALUES(945,'utwu-000283');

INSERT INTO external_track_utwu VALUES(946,'utwu-000282');

INSERT INTO external_track_utwu VALUES(947,'utwu-000281');

INSERT INTO external_track_utwu VALUES(948,'utwu-000278');

INSERT INTO external_track_utwu VALUES(949,'utwu-000277');

INSERT INTO external_track_utwu VALUES(950,'utwu-000276');

INSERT INTO external_track_utwu VALUES(951,'utwu-000275');

INSERT INTO external_track_utwu VALUES(952,'utwu-000273');

INSERT INTO external_track_utwu VALUES(953,'utwu-000271');

INSERT INTO external_track_utwu VALUES(954,'utwu-000270');

INSERT INTO external_track_utwu VALUES(955,'utwu-000268');

INSERT INTO external_track_utwu VALUES(956,'utwu-000265');

INSERT INTO external_track_utwu VALUES(957,'utwu-000264');

INSERT INTO external_track_utwu VALUES(958,'utwu-000263');

INSERT INTO external_track_utwu VALUES(959,'utwu-000262');

INSERT INTO external_track_utwu VALUES(960,'utwu-000261');

INSERT INTO external_track_utwu VALUES(961,'utwu-000260');

INSERT INTO external_track_utwu VALUES(962,'utwu-000259');

INSERT INTO external_track_utwu VALUES(963,'utwu-000258');

INSERT INTO external_track_utwu VALUES(964,'utwu-000257');

INSERT INTO external_track_utwu VALUES(965,'utwu-000252');

INSERT INTO external_track_utwu VALUES(966,'utwu-000251');

INSERT INTO external_track_utwu VALUES(967,'utwu-000250');

INSERT INTO external_track_utwu VALUES(968,'utwu-000249');

INSERT INTO external_track_utwu VALUES(969,'utwu-000244');

INSERT INTO external_track_utwu VALUES(970,'utwu-000243');

INSERT INTO external_track_utwu VALUES(971,'utwu-000242');

INSERT INTO external_track_utwu VALUES(972,'utwu-000241');

INSERT INTO external_track_utwu VALUES(973,'utwu-000237');

INSERT INTO external_track_utwu VALUES(974,'utwu-000233');

INSERT INTO external_track_utwu VALUES(975,'utwu-000223');

INSERT INTO external_track_utwu VALUES(976,'utwu-000219');

INSERT INTO external_track_utwu VALUES(977,'utwu-000215');

INSERT INTO external_track_utwu VALUES(978,'utwu-000207');

INSERT INTO external_track_utwu VALUES(979,'utwu-000206');

INSERT INTO external_track_utwu VALUES(980,'utwu-000203');

INSERT INTO external_track_utwu VALUES(981,'utwu-000202');

INSERT INTO external_track_utwu VALUES(982,'utwu-000201');

INSERT INTO external_track_utwu VALUES(983,'utwu-000200');

INSERT INTO external_track_utwu VALUES(984,'utwu-000195');

INSERT INTO external_track_utwu VALUES(985,'utwu-000194');

INSERT INTO external_track_utwu VALUES(986,'utwu-000193');

INSERT INTO external_track_utwu VALUES(987,'utwu-000192');

INSERT INTO external_track_utwu VALUES(988,'utwu-000191');

INSERT INTO external_track_utwu VALUES(989,'utwu-000188');

INSERT INTO external_track_utwu VALUES(990,'utwu-000187');

INSERT INTO external_track_utwu VALUES(991,'utwu-000186');

INSERT INTO external_track_utwu VALUES(992,'utwu-000185');

INSERT INTO external_track_utwu VALUES(993,'utwu-000184');

INSERT INTO external_track_utwu VALUES(994,'utwu-000183');

INSERT INTO external_track_utwu VALUES(995,'utwu-000182');

INSERT INTO external_track_utwu VALUES(996,'utwu-000181');

INSERT INTO external_track_utwu VALUES(997,'utwu-000179');

INSERT INTO external_track_utwu VALUES(998,'utwu-000177');

INSERT INTO external_track_utwu VALUES(999,'utwu-000176');

INSERT INTO external_track_utwu VALUES(1000,'utwu-000175');

INSERT INTO external_track_utwu VALUES(1001,'utwu-000173');

INSERT INTO external_track_utwu VALUES(1002,'utwu-000171');

INSERT INTO external_track_utwu VALUES(1003,'utwu-000170');

INSERT INTO external_track_utwu VALUES(1004,'utwu-000169');

INSERT INTO external_track_utwu VALUES(1005,'utwu-000168');

INSERT INTO external_track_utwu VALUES(1006,'utwu-000167');

INSERT INTO external_track_utwu VALUES(1007,'utwu-000166');

INSERT INTO external_track_utwu VALUES(1008,'utwu-000165');

INSERT INTO external_track_utwu VALUES(1009,'utwu-000164');

INSERT INTO external_track_utwu VALUES(1010,'utwu-000163');

INSERT INTO external_track_utwu VALUES(1011,'utwu-000162');

INSERT INTO external_track_utwu VALUES(1012,'utwu-000161');

INSERT INTO external_track_utwu VALUES(1013,'utwu-000160');

INSERT INTO external_track_utwu VALUES(1014,'utwu-000159');

INSERT INTO external_track_utwu VALUES(1015,'utwu-000158');

INSERT INTO external_track_utwu VALUES(1016,'utwu-000157');

INSERT INTO external_track_utwu VALUES(1017,'utwu-000156');

INSERT INTO external_track_utwu VALUES(1018,'utwu-000155');

INSERT INTO external_track_utwu VALUES(1019,'utwu-000154');

INSERT INTO external_track_utwu VALUES(1020,'utwu-000152');

INSERT INTO external_track_utwu VALUES(1021,'utwu-000151');

INSERT INTO external_track_utwu VALUES(1022,'utwu-000149');

INSERT INTO external_track_utwu VALUES(1023,'utwu-000148');

INSERT INTO external_track_utwu VALUES(1024,'utwu-000144');

INSERT INTO external_track_utwu VALUES(1025,'utwu-000143');

INSERT INTO external_track_utwu VALUES(1026,'utwu-000142');

INSERT INTO external_track_utwu VALUES(1027,'utwu-000141');

INSERT INTO external_track_utwu VALUES(1028,'utwu-000138');

INSERT INTO external_track_utwu VALUES(1029,'utwu-000137');

INSERT INTO external_track_utwu VALUES(1030,'utwu-000136');

INSERT INTO external_track_utwu VALUES(1031,'utwu-000135');

INSERT INTO external_track_utwu VALUES(1032,'utwu-000134');

INSERT INTO external_track_utwu VALUES(1033,'utwu-000011');

CREATE INDEX idx_external_track_utwu_utwu_id ON external_track_utwu (utwu_id);

