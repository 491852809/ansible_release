-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: 192.168.1.100    Database: openapi_log
-- ------------------------------------------------------
-- Server version	5.5.40-log

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
-- Table structure for table `log_common`
--

DROP TABLE IF EXISTS `log_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_common` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=34179 DEFAULT CHARSET=utf8 COMMENT='通用';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_common`
--

LOCK TABLES `log_common` WRITE;
/*!40000 ALTER TABLE `log_common` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_damo`
--

DROP TABLE IF EXISTS `log_damo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_damo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='大漠';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_damo`
--

LOCK TABLES `log_damo` WRITE;
/*!40000 ALTER TABLE `log_damo` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_damo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_error`
--

DROP TABLE IF EXISTS `log_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_error` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL COMMENT '出错的文件',
  `method` varchar(100) DEFAULT NULL COMMENT '类与方法',
  `message` text COMMENT '报错信息',
  `trace` text NOT NULL COMMENT '文件追踪',
  `category` varchar(100) DEFAULT NULL COMMENT '分类',
  `created_date` datetime DEFAULT NULL,
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`)
) ENGINE=InnoDB AUTO_INCREMENT=7067 DEFAULT CHARSET=utf8 COMMENT='错误日志';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_error`
--

LOCK TABLES `log_error` WRITE;
/*!40000 ALTER TABLE `log_error` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_jidiaotong`
--

DROP TABLE IF EXISTS `log_jidiaotong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_jidiaotong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='计调通';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_jidiaotong`
--

LOCK TABLES `log_jidiaotong` WRITE;
/*!40000 ALTER TABLE `log_jidiaotong` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_jidiaotong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_meituan`
--

DROP TABLE IF EXISTS `log_meituan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_meituan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '关键字',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=2110 DEFAULT CHARSET=utf8 COMMENT='美团';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_meituan`
--

LOCK TABLES `log_meituan` WRITE;
/*!40000 ALTER TABLE `log_meituan` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_meituan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_openapi`
--

DROP TABLE IF EXISTS `log_openapi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_openapi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '关键字',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=110932 DEFAULT CHARSET=utf8 COMMENT='OpenApi V1.x~';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_openapi`
--

LOCK TABLES `log_openapi` WRITE;
/*!40000 ALTER TABLE `log_openapi` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_openapi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_qunar`
--

DROP TABLE IF EXISTS `log_qunar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_qunar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=29563 DEFAULT CHARSET=utf8 COMMENT='去哪儿';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_qunar`
--

LOCK TABLES `log_qunar` WRITE;
/*!40000 ALTER TABLE `log_qunar` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_qunar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_taobao`
--

DROP TABLE IF EXISTS `log_taobao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_taobao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='淘宝';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_taobao`
--

LOCK TABLES `log_taobao` WRITE;
/*!40000 ALTER TABLE `log_taobao` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_taobao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_way`
--

DROP TABLE IF EXISTS `log_way`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_way` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(600) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `params` text,
  `comment` text,
  `created_date` datetime DEFAULT NULL,
  `category` varchar(100) DEFAULT '' COMMENT '分类',
  `server_ip` varchar(60) DEFAULT '' COMMENT '服务器ip',
  `level` varchar(100) DEFAULT '' COMMENT '日志等级',
  `search_val` varchar(100) DEFAULT '' COMMENT '要进行搜索的值',
  PRIMARY KEY (`id`),
  KEY `created_date` (`created_date`),
  KEY `category` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=5690 DEFAULT CHARSET=utf8 COMMENT='淘在路上';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_way`
--

LOCK TABLES `log_way` WRITE;
/*!40000 ALTER TABLE `log_way` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_way` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-27  9:05:59
