USE mydata;
DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `product_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `recom_info` varchar(100) NOT NULL,
  `product_info` varchar(10) NOT NULL,
  `provider` varchar(20) NOT NULL,
  `register_date`  tinyint UNSIGNED NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- CREATE TABLE `reply` (
--   `post_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
--   `headline` varchar(100) NOT NULL,
--   `reply_num` varchar(10) NOT NULL,
--   `post_provider` varchar(20) NOT NULL,
--   `view_num`  tinyint UNSIGNED NOT NULL,
--   PRIMARY KEY (`post_id`)
-- )
SELECT * FROM post;
SELECT * FROM reply;