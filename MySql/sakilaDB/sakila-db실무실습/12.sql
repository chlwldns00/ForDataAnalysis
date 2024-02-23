USE jiun;
DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_info` (
  `product_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  ` varchar(200) NOT NULL,
  `ori_price` int NOT NULL,
  `dis_price` int NOT NULL,
  `discount_percent` int NOT NULL,
  `provider` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`item_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;