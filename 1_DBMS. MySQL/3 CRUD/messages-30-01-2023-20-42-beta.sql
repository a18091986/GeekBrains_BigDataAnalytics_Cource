-- MariaDB dump 10.19  Distrib 10.5.12-MariaDB, for Linux (x86_64)
--
-- Host: mysql.hostinger.ro    Database: u574849695_23
-- ------------------------------------------------------
-- Server version	10.5.12-MariaDB-cll-lve

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `from_user_id` int(11) NOT NULL,
  `to_user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `from_user_id` (`from_user_id`),
  KEY `to_user_id` (`to_user_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`to_user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Et molestiae commodi ipsum quod. Voluptatem sint labore omnis dolor quis in. Quo molestias qui quidem esse. Rem et quibusdam corrupti itaque.',88,18,'1979-01-25 09:36:20'),(2,'Magnam voluptate sequi facere incidunt delectus placeat et. Quo consequatur quis quis ut voluptas qui. Dicta enim qui non nulla ut sit.',97,19,'1978-08-27 17:27:00'),(3,'Magnam dignissimos officiis quia aliquid est recusandae. Delectus aut facilis aut dolores et. Non voluptates nostrum reiciendis repudiandae neque. Quas cum voluptatum exercitationem repellat.',52,10,'2001-12-19 16:04:22'),(4,'Temporibus ipsum magni rerum quis. Consequatur est fuga ipsum. Repellat animi necessitatibus molestiae voluptas voluptates. Sunt reiciendis porro autem.',28,8,'2005-12-04 06:07:54'),(5,'Dolore tempore dignissimos hic facilis sed qui. Praesentium eum sed et eaque. Qui sint qui aut officia. Sequi eveniet repudiandae in veritatis et voluptatem.',18,2,'1981-05-19 01:58:46'),(6,'Eius consequatur voluptatem aliquam dolorem voluptatem. Ab ducimus maxime qui est eum.',82,65,'1976-12-12 14:49:01'),(7,'Deserunt odio nesciunt sint eos dolorem. Veritatis voluptatem similique sunt debitis. Nobis cupiditate ipsum voluptates labore voluptatem dolor ipsum. Impedit minus beatae vel cumque nam neque cumque.',51,75,'2012-09-07 20:59:26'),(8,'Ullam quae dolor corporis sequi perspiciatis assumenda est. Est ipsa molestiae explicabo ullam.',49,69,'1979-11-09 11:40:53'),(9,'Nobis perferendis voluptates sit assumenda est. Doloribus fugit facilis perspiciatis iste nulla consequatur voluptatem est. Quisquam quis quibusdam et asperiores commodi.',36,16,'1998-03-18 07:06:06'),(10,'Nostrum ratione in pariatur consectetur dignissimos qui. Qui in enim commodi accusamus distinctio sed omnis iusto. Omnis sed autem quis fugiat error.',47,92,'1980-05-01 03:58:27'),(11,'Rem qui et omnis dolor sit id vel. Unde error sed qui nostrum et. Harum saepe perspiciatis in aliquid consectetur a repellendus. Est eius vel laborum accusamus quas.',26,28,'2001-07-23 12:43:33'),(12,'Sit officiis expedita debitis. Vel omnis voluptatem illo enim excepturi dolor. Nulla aut enim iure veniam. Rerum id error harum et sunt.',19,72,'2004-12-13 21:52:48'),(13,'Nostrum ab facilis magni omnis. Et iure voluptas laborum voluptas iste et. Possimus eos molestiae doloremque ducimus aspernatur assumenda magnam.',33,16,'1970-04-01 08:38:23'),(14,'Voluptate ducimus sint ut est nihil. Totam quis sed ab dignissimos. Nemo maxime quasi non sit suscipit incidunt praesentium.',92,71,'1977-01-12 16:05:43'),(15,'Aperiam omnis aliquam dolores nihil. Iure quia et eos nemo recusandae necessitatibus dolorum. Ut exercitationem sit accusamus impedit sunt rem voluptate.',56,76,'1980-10-20 15:16:23'),(16,'Et explicabo porro non. Perferendis iure ut illo veritatis est voluptate aut. Repellendus et eos ab. Eveniet suscipit sit neque voluptate rerum sunt ipsam.',47,90,'1976-03-16 23:55:20'),(17,'Nemo sed et aspernatur dolore aperiam. Porro itaque voluptatum quia. Repellat ab ipsa quia atque minus consequatur. Totam error enim sapiente expedita est corporis et.',45,51,'2014-06-26 04:19:32'),(18,'Ad nihil voluptas nobis. Ut nisi corporis fugit qui sunt eos dicta. Odio dolore laboriosam eligendi. Et explicabo enim sit debitis.',72,73,'2013-11-09 00:36:24'),(19,'Illum fugiat rerum sunt beatae quasi omnis repudiandae. Exercitationem sit at iusto officiis exercitationem. Sit autem nesciunt est. Occaecati aut nihil quia.',83,83,'2007-03-21 02:51:00'),(20,'Omnis quidem cupiditate accusantium a et. Harum eos voluptatem illum commodi culpa error aut. Porro perspiciatis distinctio aliquam sit dignissimos.',71,91,'1972-12-02 21:47:26'),(21,'Similique qui et temporibus et rerum. Laudantium ut ut facilis quia maxime asperiores rem. Qui ea voluptas doloremque fugiat et.',53,40,'1997-02-02 04:23:02'),(22,'Repellat consequatur quisquam facere suscipit ullam officia sint. Adipisci voluptatem neque deserunt aut vel ut occaecati. Nam cumque veniam unde.',42,71,'2001-11-03 19:35:14'),(23,'Et recusandae error quis quia ab culpa eos. Saepe culpa qui sint omnis dolores rerum. Saepe cum cumque quasi sapiente.',5,8,'1993-05-06 17:28:43'),(24,'Facere voluptas minus voluptatem. Molestiae in sit repudiandae facere vel sit quidem molestiae. Vel sunt eum ullam consequatur aperiam. Assumenda voluptatum tempora rem sunt expedita.',49,35,'1978-03-24 16:58:05'),(25,'Doloribus sapiente amet eos atque et et. Voluptates enim dolorem aspernatur beatae ea reprehenderit dolor quod. Assumenda consequatur accusantium error.',6,33,'1992-10-11 06:16:50'),(26,'Quis qui ipsam suscipit repellendus rerum voluptas. Quod voluptatibus hic quis velit sed neque est. Ut molestiae voluptate pariatur molestiae et aut maiores fugit.',41,81,'2009-09-30 07:34:25'),(27,'Debitis sit dolores eos est est non tempore. Et iste qui voluptatem officiis nihil. Odit inventore in libero sit quisquam sunt. Quo tempora nisi laboriosam.',63,92,'2003-08-14 02:32:32'),(28,'Quis maxime aspernatur voluptas itaque sed. Sint non et ut aut ut. Esse praesentium consequatur quia quaerat harum ut nulla et. Ipsam aliquam doloribus reprehenderit fugiat id rerum et. Distinctio reprehenderit cum voluptatem in cupiditate dolorum aut.',22,63,'1974-10-24 17:40:59'),(29,'Aut fugit expedita esse fuga voluptate. Totam consequatur unde quia consequatur et delectus. Consequatur qui sed voluptatum debitis. Harum vel dolores maxime dolores maiores et natus.',54,90,'1971-01-20 20:58:57'),(30,'Rerum nesciunt quia dignissimos. Et nostrum ad qui. Enim consequatur aperiam omnis aut. Architecto sunt doloribus sunt.',49,6,'2022-12-18 08:14:17'),(31,'Dolores perspiciatis quae doloribus necessitatibus voluptas ea est. Est qui sunt dolorem praesentium. Cupiditate beatae iusto dolore sint. Sapiente aliquam voluptatem dicta voluptatum eligendi aliquam.',55,23,'2012-09-04 03:56:23'),(32,'Cum dolorem dolores vitae est placeat blanditiis maiores. Quasi animi aut qui qui recusandae eligendi esse. Dignissimos quas animi tenetur tenetur error amet. Ut non laudantium a dolore beatae qui molestiae.',51,6,'1998-08-23 16:09:46'),(33,'Consequatur facilis a molestiae. Voluptatibus et accusamus esse numquam.',32,76,'2015-10-23 12:38:05'),(34,'Quibusdam autem sint et magnam beatae et. Nemo voluptatem sunt qui. Voluptatum consequatur nihil veritatis cupiditate nihil sed et.',12,91,'1999-10-20 03:38:16'),(35,'Ullam quia ut dolor asperiores quo laboriosam. Quaerat ut harum soluta magni voluptatem. At omnis exercitationem qui inventore. Est nostrum enim ipsa error quam.',83,12,'2004-10-24 09:35:50'),(36,'Velit est ducimus unde ab aliquid et maiores. Reprehenderit at ab qui aperiam qui voluptate vitae. Id consequatur qui numquam et mollitia.',90,84,'2012-02-06 11:06:52'),(37,'Nemo eius dolores asperiores doloribus et ipsam. Corrupti iure aliquam numquam impedit consequatur minima sed. Aspernatur illo quisquam delectus modi qui.',76,44,'1997-03-05 05:02:47'),(38,'Sapiente a nihil nisi error. Tempora at vitae et dolorum ut quo aut.',79,25,'1986-08-27 07:14:30'),(39,'Doloribus voluptate totam sequi quibusdam labore labore maiores. Praesentium explicabo tempore eum. Aliquam natus id quis eveniet repellendus dolorem voluptatum.',11,61,'1983-01-08 13:54:41'),(40,'Ratione expedita voluptas est sit rem nesciunt fuga. Laboriosam maxime voluptatem odit. Sapiente tempora sed soluta aperiam sed.',61,13,'2017-01-18 01:21:57'),(41,'Illo ea sequi sed ex cumque sit illum. Consequatur asperiores ut delectus qui rerum velit tenetur. Culpa consequatur sit dolores sed illo.',52,13,'1990-07-05 21:31:49'),(42,'Iusto saepe quos unde vel aliquid. Enim nostrum ut molestiae voluptas. Quisquam non unde aut quia adipisci error sed quas.',7,44,'2021-05-25 04:53:53'),(43,'Maiores voluptatibus fuga voluptatem eveniet inventore enim. Doloribus et animi quaerat deleniti sit laboriosam soluta. Ipsum blanditiis ullam non quia deleniti qui sunt. Deserunt aliquam dolor veniam officia perferendis.',80,100,'2010-03-15 12:25:13'),(44,'Quia aut qui blanditiis. Aliquid ipsam saepe enim fugit fugiat aut. Tempore saepe quia cumque consequatur aut.',1,25,'2012-01-02 17:06:20'),(45,'Placeat laudantium porro nisi recusandae accusamus asperiores. Maxime excepturi nihil et ea. Adipisci eum dolorem distinctio. Et in repudiandae qui aut quam.',70,94,'1990-09-18 23:55:09'),(46,'Tempore deleniti esse est quia dignissimos. Totam et temporibus fugiat perspiciatis et dolorem quo dolores. Facilis et deleniti quia fuga numquam ut.',30,71,'1971-07-23 17:24:03'),(47,'Voluptas hic cum doloribus incidunt quia ut veniam facere. Et sit soluta ut quidem corrupti eaque omnis. Autem et velit nostrum odio amet.',34,13,'2008-01-28 14:20:33'),(48,'Minima ullam rerum ea enim et ratione eum tenetur. Quis porro voluptas similique nihil voluptas nihil dolores. Voluptates eum aut tenetur et neque distinctio facilis.',51,74,'1972-10-25 01:49:41'),(49,'Minima eos nisi ut et molestias. Sit sequi aut impedit sed quod. Qui cumque corrupti quidem. Magni et eaque ipsum et porro inventore nulla nesciunt.',56,8,'1978-07-27 04:29:14'),(50,'Sed voluptate optio explicabo quo. Repudiandae adipisci optio aut dolorem.',5,41,'1981-11-01 00:04:58'),(51,'Eum omnis voluptatibus similique repellendus iste exercitationem ratione laudantium. Distinctio voluptatem id cumque odit cupiditate quos sequi. Nesciunt dignissimos beatae vel eum.',74,50,'2012-09-19 20:29:29'),(52,'Sed consequatur animi ut sit laborum quis ipsum. Libero cum totam eos beatae adipisci ut. Laboriosam distinctio minus possimus velit.',30,26,'2003-01-15 01:38:32'),(53,'Inventore aut explicabo et quo voluptas rem corporis. Omnis quidem iure sed maxime. Provident molestiae blanditiis praesentium dolorem ducimus voluptas laudantium libero.',10,32,'2000-01-17 01:10:47'),(54,'Nihil illo reprehenderit architecto consequuntur repudiandae. Veniam rem omnis minima aut. Molestiae dicta quidem ut sint animi qui.',93,51,'1978-07-11 10:50:11'),(55,'Dolor modi quae occaecati facere. Sint quae voluptatem laudantium exercitationem sit. Aut pariatur officia molestiae nisi voluptas velit.',40,40,'1990-05-26 04:17:55'),(56,'Minus quo distinctio nemo optio dolor consequatur. Nihil voluptas a sed laudantium ut. Error voluptatem non autem quia nihil eaque consectetur.',81,56,'1984-01-28 01:23:42'),(57,'Aut quibusdam dignissimos mollitia minima. Non minus dicta sit voluptatem est modi. Sunt aut aut delectus earum. Beatae minus laudantium in nesciunt dolorem dolores et.',75,15,'2017-02-03 22:56:54'),(58,'Voluptas corporis reiciendis nostrum ipsum temporibus voluptatem. Ullam qui maxime corrupti iure accusantium accusantium. Ipsum nam sed mollitia est. Vel laudantium eos quasi ratione.',60,36,'2002-10-21 23:54:30'),(59,'Ullam eaque et harum non qui illum. Necessitatibus ea aut cupiditate. Quia nostrum soluta enim qui natus nam nihil nihil. Iste officia ut eius voluptatem itaque.',49,45,'2012-05-03 02:18:48'),(60,'Quia quae quia minima ab sit est et. Sint aperiam distinctio qui voluptatem sed explicabo minima.',33,86,'2015-03-23 02:44:13'),(61,'Voluptas sit quis impedit accusamus similique. Recusandae fugiat nam reprehenderit ratione non.',83,25,'2021-06-18 09:56:19'),(62,'Excepturi aut in maiores ut. Eius asperiores optio doloribus voluptas ut enim ut. Reiciendis expedita occaecati voluptate exercitationem natus.',61,37,'2018-02-05 02:50:56'),(63,'Est est expedita hic velit. Itaque reprehenderit impedit voluptatibus adipisci. Sequi consequatur illum autem quam.',7,26,'2012-03-06 21:45:31'),(64,'Minus accusamus in eum voluptatem. Facilis omnis nam perferendis. Soluta laborum rerum reprehenderit assumenda. Fugit laboriosam fugit ducimus reiciendis.',52,97,'1971-09-02 17:09:06'),(65,'Recusandae quas autem eos tempore culpa aut delectus iste. Ea et quasi est qui dignissimos. Necessitatibus temporibus sed quas atque. Occaecati est aperiam iste necessitatibus exercitationem officia ratione expedita. At optio quia et maxime aspernatur.',81,33,'1987-11-12 10:47:34'),(66,'Nam tenetur et voluptatibus. Aut voluptatem ut quasi enim repellendus repellendus. Nesciunt sint alias et similique cum omnis omnis. Tenetur quasi necessitatibus libero sit maxime ut.',11,1,'1987-11-29 00:27:38'),(67,'Recusandae omnis iusto impedit quia veritatis suscipit ipsum nulla. Quis enim beatae maxime sit dolor cum. Alias maiores nesciunt est aut id voluptates. Quis iure molestiae et non adipisci delectus tempore. Sint ullam perspiciatis dolor mollitia voluptates molestiae libero.',53,92,'2007-02-28 07:10:00'),(68,'Id aliquam hic eos enim quis iste saepe. Aliquid quas ipsum soluta sed officia.',53,44,'2016-01-17 20:13:32'),(69,'Numquam est nostrum sit debitis rem. Id consequuntur quia quibusdam alias. Veniam vel laudantium repellat. Quaerat molestias asperiores sit nulla commodi. Velit hic mollitia saepe accusantium maxime.',32,87,'1981-04-19 09:19:48'),(70,'Dolorum distinctio quia eum aliquid consequatur minus qui necessitatibus. At nemo cum et voluptates ut eos optio commodi. Deleniti ut pariatur ut dolores cumque temporibus aut. Explicabo dicta nemo eum est.',95,55,'1995-09-19 00:56:26'),(71,'Alias aut temporibus nesciunt ab nihil enim. Quibusdam ipsa laudantium qui adipisci consequatur et. Veritatis labore alias totam et. Quia quia laudantium vero vitae laborum quaerat.',23,40,'2003-09-11 09:58:58'),(72,'Aut sed fugiat enim dolorem fugit. Exercitationem nisi nihil necessitatibus qui. Quas enim velit consequatur sapiente delectus autem dolorem. Blanditiis maiores rerum odit.',90,4,'2007-12-18 07:05:57'),(73,'Id animi quaerat nulla. Occaecati rerum deserunt cupiditate quis suscipit tenetur. Totam repudiandae molestiae aperiam eum consequatur facere. Eos iure veniam dolorem aperiam voluptatum veniam excepturi. Et sed ratione ea velit quia iusto sed dolores.',94,55,'1986-04-13 09:15:59'),(74,'Laudantium qui accusantium porro reprehenderit esse. Iusto sint itaque veniam perferendis. Ipsa similique veniam laudantium modi aut voluptas. Similique est dolorem dolor perferendis non omnis.',95,85,'1983-04-01 12:02:36'),(75,'Assumenda amet odit dignissimos temporibus ut numquam. Earum dolores tenetur saepe ea eum eveniet iste. Et natus nihil beatae autem quo. Non molestiae ratione vel tempore nostrum reprehenderit veniam.',37,99,'1995-09-22 18:08:00'),(76,'Molestiae provident sit quia dolor exercitationem. Quis voluptatem pariatur labore fugiat sequi ut sit quidem. Neque quidem error debitis fuga harum et quis aliquam. Ut tenetur a velit eaque.',56,79,'1981-05-27 10:04:26'),(77,'Totam quibusdam ipsum beatae incidunt et dolores occaecati consequuntur. Quibusdam aut nulla sapiente. Ullam officiis magnam rem ducimus voluptatem illum.',9,57,'2007-06-27 17:20:07'),(78,'Et laboriosam qui voluptas autem aliquam. Non rerum voluptatem quia reprehenderit itaque quod dignissimos. Rerum sunt recusandae repudiandae libero modi reprehenderit nemo et.',47,20,'2019-10-01 10:52:16'),(79,'Pariatur dolores pariatur exercitationem quia. Et et autem nihil accusantium qui voluptatem non.',96,81,'2010-06-23 07:16:58'),(80,'Libero sed sit odit voluptas dolorem id. Veritatis iusto eaque soluta. Magnam sint perferendis suscipit amet officia.',50,38,'2007-08-17 09:31:00'),(81,'Voluptas facilis repellendus voluptatem aut consequatur in. Facere voluptatem facilis laborum fugiat ut sit tenetur minus. Aut possimus aspernatur quia voluptatem id. Maxime et qui est nulla dolores atque est veritatis.',48,77,'1981-07-06 09:36:49'),(82,'Est deserunt aperiam ipsa blanditiis cumque sint veniam. Laudantium nisi recusandae ea voluptatibus nam qui. Recusandae nihil iusto eveniet aut enim repudiandae.',23,13,'2012-04-02 19:16:40'),(83,'Ut autem minus consequatur praesentium. Ut dolor quia consectetur veritatis magni. Aliquam et minima facilis accusantium illo enim maxime ut.',64,62,'1992-10-20 02:14:07'),(84,'Debitis ducimus repudiandae laboriosam et. Earum eius id laudantium nobis. Ullam quis consequatur molestiae ut omnis. Non ullam consequatur quia et repellat omnis.',11,72,'2018-03-05 07:36:18'),(85,'Ad ratione magni commodi qui fuga libero. Ad placeat dignissimos est laboriosam. Voluptates quas eum et ullam ipsa id. Natus cupiditate labore asperiores possimus debitis repudiandae. Aut porro ipsum eaque minus at voluptas.',3,81,'2015-09-04 05:13:03'),(86,'Quidem aliquam dolorem consectetur deserunt. Voluptatem rerum aut atque cupiditate rerum unde exercitationem. Ut ex qui quos commodi mollitia quis sed.',87,42,'1980-02-19 23:53:41'),(87,'Doloremque consequatur ex velit id dolorem totam error voluptas. Maiores ut consequatur aspernatur expedita est. Velit ea consequuntur suscipit quia quibusdam est. Ratione natus perspiciatis et.',74,23,'1987-09-29 06:48:56'),(88,'Explicabo necessitatibus aliquid voluptatem velit. Sunt laboriosam ea consectetur cumque magni. Sed id porro nihil odio quisquam enim. Rem quaerat molestiae eos minus eos ducimus sint. Debitis soluta dolorum et et in voluptatum.',18,100,'1998-09-11 08:47:56'),(89,'Ut accusamus deserunt eligendi. Ex dolorem est inventore quidem rerum. Eos saepe eos omnis dolorum accusantium quibusdam fugit.',42,74,'1979-06-11 01:12:26'),(90,'Sapiente enim quibusdam expedita. Similique non ipsam blanditiis aut maxime reprehenderit perferendis. Soluta repellendus molestiae eligendi unde aut quo qui.',54,90,'1978-06-23 17:45:16'),(91,'Aut nulla facilis ut aliquid eum quaerat. Vero est est consequatur et dignissimos minima. Accusamus et et nihil corrupti dolore qui. In adipisci tenetur et id explicabo ea.',9,30,'2001-04-15 16:59:32'),(92,'Qui consequatur vitae sed repellat tempore velit. Ab ut quisquam tempore. Enim placeat occaecati repellendus et tempora eveniet. Repellendus sit sed qui sunt aliquid. Exercitationem impedit consequatur omnis natus quibusdam nesciunt.',46,26,'2018-12-03 01:49:34'),(93,'Quis illum qui est eum eius. Aperiam dolores laudantium veniam quisquam ut similique.',6,20,'2013-06-09 08:48:31'),(94,'Dolorum praesentium iusto provident incidunt sed qui. Cumque quaerat sit aliquid occaecati. Sunt qui omnis velit voluptatem. Voluptas repellendus neque porro.',100,85,'2010-02-05 01:20:37'),(95,'Recusandae rerum consequatur sit ad distinctio minima. Quidem et quia dicta commodi. Sit voluptas qui libero.',49,43,'2020-05-16 12:06:10'),(96,'Facilis corporis animi natus. Dolores eligendi nobis vel autem sed cupiditate voluptas. Sint dolore sunt atque hic. Laborum neque aspernatur at ut labore.',21,15,'1970-12-16 01:26:29'),(97,'Atque qui quis totam. Consequuntur omnis adipisci odit dolor ex et et est. Voluptate ut quia dolorum similique. Officia facilis quia nostrum ut delectus dolor similique.',13,23,'1983-10-05 08:57:12'),(98,'Dolorem ipsam eligendi rem magnam facere. Quaerat aliquam facilis ab et fugiat. Qui iure ratione rerum autem assumenda.',50,3,'2010-04-17 19:48:11'),(99,'Sed dolor in dolor. Incidunt ullam sapiente occaecati ut. Saepe saepe nihil ut harum dolorum. Dolor ut officiis pariatur qui. Accusamus cupiditate ipsum reprehenderit quam quia sed.',100,45,'2004-11-04 20:26:31'),(100,'Quaerat dolor in autem culpa et quis qui. Facilis maiores non consequuntur dignissimos numquam. Et tempore rerum possimus quisquam. Voluptas odio animi repellendus asperiores facilis.',15,44,'1988-11-19 22:03:06');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-30 20:42:28
