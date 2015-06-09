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
  `sid` int(11) NOT NULL COMMENT '服务ID\n',
  `s_state` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  `mileage` int(11) NOT NULL DEFAULT '0',
  `start_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `end_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='记录一次服务记录\n';
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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

-- Dump completed on 2015-06-09 16:43:31
