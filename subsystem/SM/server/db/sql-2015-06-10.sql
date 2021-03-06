CREATE DATABASE  IF NOT EXISTS `db_zebra_sm` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `db_zebra_sm`;
-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: db_zebra_sm
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_service`
--

DROP TABLE IF EXISTS `t_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_service` (
  `sid` INT(11) NOT NULL AUTO_INCREMENT
  COMMENT '服务ID\n',
  `s_state` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  `mileage` int(11) NOT NULL DEFAULT '0',
  `start_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `end_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`sid`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 10000000
  DEFAULT CHARSET = utf8
  COMMENT = '记录一次服务记录\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_service`
--

LOCK TABLES `t_service` WRITE;
/*!40000 ALTER TABLE `t_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `uid` int(11) NOT NULL COMMENT '用户ID\n',
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(50) NOT NULL COMMENT '密码\n',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '帐户的创建时间 \n',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `phone_UNIQUE` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户登录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (1433822443,'15652750943','27b5cb718d7c4685cf89e6227214402ec5bdbe26','2015-06-09 04:00:43'),(1433912046,'15652750922','d91c6e290a945b908ac216c32bbdc57ec5128c3f','2015-06-10 04:54:06'),(1433985189,'15652750950','c7b84b40135b8cf58a86bf6eae9fe89a9785d0fd','2015-06-11 01:13:09');
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user_info`
--

DROP TABLE IF EXISTS `t_user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_info` (
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `sex` int(11) DEFAULT NULL COMMENT '用户性别',
  `occupation` varchar(50) DEFAULT NULL COMMENT '职业',
  `head` varchar(50) DEFAULT NULL COMMENT '头像',
  `cert_id` varchar(50) DEFAULT NULL COMMENT '身份证',
  `fraction` int(11) NOT NULL DEFAULT '0' COMMENT '用户积分',
  `level` int(11) NOT NULL DEFAULT '0' COMMENT '用户等级',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `cert_id_UNIQUE` (`cert_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user_info`
--

LOCK TABLES `t_user_info` WRITE;
/*!40000 ALTER TABLE `t_user_info` DISABLE KEYS */;
INSERT INTO `t_user_info` VALUES (1433822443,NULL,NULL,NULL,NULL,NULL,0,0),(1433912046,NULL,NULL,NULL,NULL,NULL,0,0),(1433985189,NULL,NULL,NULL,NULL,NULL,0,0);
/*!40000 ALTER TABLE `t_user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user_state`
--

DROP TABLE IF EXISTS `t_user_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_state` (
  `uid` int(11) NOT NULL DEFAULT '0',
  `online_state` int(11) NOT NULL DEFAULT '0' COMMENT '在线状态',
  `lng` double unsigned NOT NULL DEFAULT '999' COMMENT '经度',
  `lat` double NOT NULL DEFAULT '999' COMMENT '纬度',
  `service_state` int(11) NOT NULL DEFAULT '0' COMMENT '服务状态',
  `is_debts` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否欠费',
  `total_mileage` int(11) DEFAULT '0',
  `total_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user_state`
--

LOCK TABLES `t_user_state` WRITE;
/*!40000 ALTER TABLE `t_user_state` DISABLE KEYS */;
INSERT INTO `t_user_state` VALUES (123456,0,999,999,0,0,0,0),(1433775135,0,999,999,0,0,0,0),(1433776925,0,999,999,0,0,0,0),(1433776985,0,999,999,0,0,0,0),(1433779175,0,999,999,0,0,0,0),(1433779206,0,999,999,0,0,0,0),(1433822443,0,999,999,0,0,0,0),(1433912046,0,999,999,0,0,0,0),(1433985189,0,999,999,0,0,0,0);
/*!40000 ALTER TABLE `t_user_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db_zebra_sm'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-11  9:25:05
