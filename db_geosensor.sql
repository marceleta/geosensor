-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: db_geosensor
-- ------------------------------------------------------
-- Server version	5.5.5-10.7.3-MariaDB-1:10.7.3+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `area_area`
--

DROP TABLE IF EXISTS `area_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area_area` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `nome` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  `descricao` varchar(300) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_area`
--

/*!40000 ALTER TABLE `area_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `area_area` ENABLE KEYS */;

--
-- Table structure for table `area_ponto`
--

DROP TABLE IF EXISTS `area_ponto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area_ponto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `lat` double NOT NULL,
  `lng` double NOT NULL,
  `centro_area` tinyint(1) DEFAULT NULL,
  `area_id` bigint(20) DEFAULT NULL,
  `rua_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `area_ponto_area_id_86505ee2_fk_area_area_id` (`area_id`),
  KEY `area_ponto_rua_id_08a00b08_fk_area_rua_id` (`rua_id`),
  CONSTRAINT `area_ponto_area_id_86505ee2_fk_area_area_id` FOREIGN KEY (`area_id`) REFERENCES `area_area` (`id`),
  CONSTRAINT `area_ponto_rua_id_08a00b08_fk_area_rua_id` FOREIGN KEY (`rua_id`) REFERENCES `area_rua` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_ponto`
--

/*!40000 ALTER TABLE `area_ponto` DISABLE KEYS */;
/*!40000 ALTER TABLE `area_ponto` ENABLE KEYS */;

--
-- Table structure for table `area_rua`
--

DROP TABLE IF EXISTS `area_rua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area_rua` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `nome` varchar(30) COLLATE utf8mb3_bin NOT NULL,
  `a_rea_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `area_rua_a_rea_id_dc8c5fa3_fk_area_area_id` (`a_rea_id`),
  CONSTRAINT `area_rua_a_rea_id_dc8c5fa3_fk_area_area_id` FOREIGN KEY (`a_rea_id`) REFERENCES `area_area` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_rua`
--

/*!40000 ALTER TABLE `area_rua` DISABLE KEYS */;
/*!40000 ALTER TABLE `area_rua` ENABLE KEYS */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add trator',7,'add_trator'),(26,'Can change trator',7,'change_trator'),(27,'Can delete trator',7,'delete_trator'),(28,'Can view trator',7,'view_trator'),(29,'Can add sensor',8,'add_sensor'),(30,'Can change sensor',8,'change_sensor'),(31,'Can delete sensor',8,'delete_sensor'),(32,'Can view sensor',8,'view_sensor'),(33,'Can add dispositivo',9,'add_dispositivo'),(34,'Can change dispositivo',9,'change_dispositivo'),(35,'Can delete dispositivo',9,'delete_dispositivo'),(36,'Can view dispositivo',9,'view_dispositivo'),(37,'Can add trabalho',10,'add_trabalho'),(38,'Can change trabalho',10,'change_trabalho'),(39,'Can delete trabalho',10,'delete_trabalho'),(40,'Can view trabalho',10,'view_trabalho'),(41,'Can add posicao',11,'add_posicao'),(42,'Can change posicao',11,'change_posicao'),(43,'Can delete posicao',11,'delete_posicao'),(44,'Can view posicao',11,'view_posicao'),(45,'Can add imagem',12,'add_imagem'),(46,'Can change imagem',12,'change_imagem'),(47,'Can delete imagem',12,'delete_imagem'),(48,'Can view imagem',12,'view_imagem'),(49,'Can add ponto',13,'add_ponto'),(50,'Can change ponto',13,'change_ponto'),(51,'Can delete ponto',13,'delete_ponto'),(52,'Can view ponto',13,'view_ponto'),(53,'Can add rua',14,'add_rua'),(54,'Can change rua',14,'change_rua'),(55,'Can delete rua',14,'delete_rua'),(56,'Can view rua',14,'view_rua'),(57,'Can add area',15,'add_area'),(58,'Can change area',15,'change_area'),(59,'Can delete area',15,'delete_area'),(60,'Can view area',15,'view_area');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$dmbXqeNxhFOEzV3yUS6miA$BKfly5HPCZbXClrQxcS2eIFB9OsN2xQ3O+39GHbQGtY=','2022-05-07 17:11:30.661616',1,'marcelo','','','marcelo.vne@gmail.com',1,1,'2022-05-07 13:21:30.278288');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

--
-- Table structure for table `dispositivo_dispositivo`
--

DROP TABLE IF EXISTS `dispositivo_dispositivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispositivo_dispositivo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `modelo` varchar(60) COLLATE utf8mb3_bin NOT NULL,
  `mac` varchar(17) COLLATE utf8mb3_bin NOT NULL,
  `trator_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dispositivo_dispositivo_trator_id_4f2d93bc_fk_trator_trator_id` (`trator_id`),
  CONSTRAINT `dispositivo_dispositivo_trator_id_4f2d93bc_fk_trator_trator_id` FOREIGN KEY (`trator_id`) REFERENCES `trator_trator` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivo_dispositivo`
--

/*!40000 ALTER TABLE `dispositivo_dispositivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `dispositivo_dispositivo` ENABLE KEYS */;

--
-- Table structure for table `dispositivo_sensor`
--

DROP TABLE IF EXISTS `dispositivo_sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispositivo_sensor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `temperatura` double NOT NULL,
  `dispositivo_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dispositivo_sensor_dispositivo_id_d9c2b1fd_fk_dispositi` (`dispositivo_id`),
  CONSTRAINT `dispositivo_sensor_dispositivo_id_d9c2b1fd_fk_dispositi` FOREIGN KEY (`dispositivo_id`) REFERENCES `dispositivo_dispositivo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivo_sensor`
--

/*!40000 ALTER TABLE `dispositivo_sensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `dispositivo_sensor` ENABLE KEYS */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_bin DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8mb3_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8mb3_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(15,'area','area'),(13,'area','ponto'),(14,'area','rua'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'dispositivo','dispositivo'),(8,'dispositivo','sensor'),(12,'imagem','imagem'),(6,'sessions','session'),(11,'trabalho','posicao'),(10,'trabalho','trabalho'),(7,'trator','trator');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-05-07 13:03:20.905718'),(2,'auth','0001_initial','2022-05-07 13:03:26.322082'),(3,'admin','0001_initial','2022-05-07 13:03:27.373801'),(4,'admin','0002_logentry_remove_auto_add','2022-05-07 13:03:27.416893'),(5,'admin','0003_logentry_add_action_flag_choices','2022-05-07 13:03:27.442988'),(6,'contenttypes','0002_remove_content_type_name','2022-05-07 13:03:28.046011'),(7,'auth','0002_alter_permission_name_max_length','2022-05-07 13:03:28.506055'),(8,'auth','0003_alter_user_email_max_length','2022-05-07 13:03:29.101820'),(9,'auth','0004_alter_user_username_opts','2022-05-07 13:03:29.143792'),(10,'auth','0005_alter_user_last_login_null','2022-05-07 13:03:29.682171'),(11,'auth','0006_require_contenttypes_0002','2022-05-07 13:03:29.702204'),(12,'auth','0007_alter_validators_add_error_messages','2022-05-07 13:03:29.734391'),(13,'auth','0008_alter_user_username_max_length','2022-05-07 13:03:29.965997'),(14,'auth','0009_alter_user_last_name_max_length','2022-05-07 13:03:30.210252'),(15,'auth','0010_alter_group_name_max_length','2022-05-07 13:03:30.638037'),(16,'auth','0011_update_proxy_permissions','2022-05-07 13:03:30.680203'),(17,'auth','0012_alter_user_first_name_max_length','2022-05-07 13:03:30.906043'),(18,'sessions','0001_initial','2022-05-07 13:03:31.662126'),(19,'trator','0001_initial','2022-05-07 13:03:31.862111'),(20,'dispositivo','0001_initial','2022-05-07 13:06:03.735595'),(21,'trabalho','0001_initial','2022-05-07 13:11:23.731261'),(22,'imagem','0001_initial','2022-05-07 13:12:52.668295'),(23,'area','0001_initial','2022-05-07 13:15:34.862461');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb3_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ykoai38tvs9qzn7rshugsfikbaqdvu1l','.eJxVjM0OgjAYBN-lZ9PwtaUFj959hmbLtoIaSPg5Gd9dSTjodWdmXypiW_u4LXmOA9VZiTr9bgndI4874B3jbdLdNK7zkPSu6IMu-joxPy-H-3fQY-m_NVjRkY0DrS9I0lrxSaTthDCuqWuYOoQEosAFVJbFGnoyBSM-q_cHAFY4ow:1nnQm2:3Rk9daxNjENCed0dbCW82-GTfy_MsmFhcXR5nCIoqh8','2022-05-21 17:11:30.678409');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

--
-- Table structure for table `imagem_imagem`
--

DROP TABLE IF EXISTS `imagem_imagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagem_imagem` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `img` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  `nome` varchar(20) COLLATE utf8mb3_bin NOT NULL,
  `north` double NOT NULL,
  `south` double NOT NULL,
  `east` double NOT NULL,
  `west` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagem_imagem`
--

/*!40000 ALTER TABLE `imagem_imagem` DISABLE KEYS */;
/*!40000 ALTER TABLE `imagem_imagem` ENABLE KEYS */;

--
-- Table structure for table `trabalho_posicao`
--

DROP TABLE IF EXISTS `trabalho_posicao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabalho_posicao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `data_hora` datetime(6) NOT NULL,
  `lat` double NOT NULL,
  `lng` double NOT NULL,
  `pressao_a` double NOT NULL,
  `pressao_b` double NOT NULL,
  `fluxo_a` double NOT NULL,
  `fluxo_b` double NOT NULL,
  `razao` int(11) NOT NULL,
  `sentido` double NOT NULL,
  `velocidade` double NOT NULL,
  `dispositivo_id` bigint(20) NOT NULL,
  `trabalho_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `trabalho_posicao_dispositivo_id_0aab6130_fk_dispositi` (`dispositivo_id`),
  KEY `trabalho_posicao_trabalho_id_2c0beda7_fk_trabalho_trabalho_id` (`trabalho_id`),
  CONSTRAINT `trabalho_posicao_dispositivo_id_0aab6130_fk_dispositi` FOREIGN KEY (`dispositivo_id`) REFERENCES `dispositivo_dispositivo` (`id`),
  CONSTRAINT `trabalho_posicao_trabalho_id_2c0beda7_fk_trabalho_trabalho_id` FOREIGN KEY (`trabalho_id`) REFERENCES `trabalho_trabalho` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabalho_posicao`
--

/*!40000 ALTER TABLE `trabalho_posicao` DISABLE KEYS */;
/*!40000 ALTER TABLE `trabalho_posicao` ENABLE KEYS */;

--
-- Table structure for table `trabalho_trabalho`
--

DROP TABLE IF EXISTS `trabalho_trabalho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabalho_trabalho` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `data` date NOT NULL,
  `h_inicio` time(6) NOT NULL,
  `h_final` time(6) NOT NULL,
  `horas_trabalhadas` time(6) NOT NULL,
  `maior_velocidade` double NOT NULL,
  `velocidade_media` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabalho_trabalho`
--

/*!40000 ALTER TABLE `trabalho_trabalho` DISABLE KEYS */;
/*!40000 ALTER TABLE `trabalho_trabalho` ENABLE KEYS */;

--
-- Table structure for table `trator_trator`
--

DROP TABLE IF EXISTS `trator_trator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trator_trator` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create` date NOT NULL,
  `modified` date NOT NULL,
  `imagem` varchar(100) COLLATE utf8mb3_bin NOT NULL,
  `descricao` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `modelo` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trator_trator`
--

/*!40000 ALTER TABLE `trator_trator` DISABLE KEYS */;
/*!40000 ALTER TABLE `trator_trator` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-07 18:50:36
