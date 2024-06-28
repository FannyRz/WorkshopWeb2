-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sudokudb
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueur` (
  `id_joueur` int NOT NULL,
  `pseudo` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `prenom` varchar(45) NOT NULL,
  `date_creation` date NOT NULL,
  `nationalite` varchar(45) NOT NULL,
  `date_naissance` date DEFAULT NULL,
  `score` int NOT NULL DEFAULT '0',
  `mot_de_passe` varchar(100) NOT NULL,
  PRIMARY KEY (`id_joueur`),
  UNIQUE KEY `id_joueur_UNIQUE` (`id_joueur`),
  UNIQUE KEY `pseudo_UNIQUE` (`pseudo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (0,'Lililica','TERRASSON','Lucas','2024-06-26','Fr','2024-06-01',0,'a47ac54472fea6fcd0e8ad9be61f8fcd0e5fb13ff686407f993f8205e0c1a3ca'),(1,'Nyny','Ruiz','Fanny','2024-06-28','Fr','2024-06-01',1857,'d41ca9b3ff93b24da439c32ab28c24fd03220fbee13d3c4650f20125172ae72d'),(2,'JUJU','Venet','Justine','2024-06-28','Fr','2024-06-12',4479,'7d1a54127b222502f5b79b5fb0803061152a44f92b37e23c6527baf665d4da9a'),(3,'Anneeeeu','PASSELEGUE','ANNE','2024-06-28','Italie','2027-03-28',335,'7d1a54127b222502f5b79b5fb0803061152a44f92b37e23c6527baf665d4da9a'),(4,'BigMAC','RONALD','McDonald','2024-06-28','EU','2019-02-28',3496,'fd19314000810517eee9bdfa0e2726705b894e74949cd62aa574cd187efd442a'),(5,'JediDu64','Star','Wars','2024-06-28','En','1998-12-25',4170,'7656d6cee73f02b73d5e02f6551b830374f8a7ed326da22406e6509a2d60c67f');
/*!40000 ALTER TABLE `joueur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `id_session` int NOT NULL,
  `nbr_erreur` int DEFAULT NULL,
  `temps` time NOT NULL,
  `date` date NOT NULL,
  `id_joueur` int NOT NULL,
  `id_sudoku` int NOT NULL,
  PRIMARY KEY (`id_session`),
  KEY `id_sudoku_idx` (`id_sudoku`),
  KEY `id_joueur_idx` (`id_joueur`),
  CONSTRAINT `id_joueur` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id_joueur`),
  CONSTRAINT `id_sudoku` FOREIGN KEY (`id_sudoku`) REFERENCES `sudoku` (`id_sudoku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (0,65454,'00:48:00','2024-05-29',0,0),(1,2,'00:21:05','2024-05-29',0,1),(2,5,'12:02:21','2024-05-29',0,2),(3,6,'00:00:25','2024-05-29',0,6),(4,4,'00:15:06','2024-05-29',1,5),(5,2,'00:52:31','2024-05-29',1,2),(6,8,'01:06:58','2024-05-29',2,1),(7,15,'00:21:31','2024-05-29',1,1),(8,4546,'00:15:06','2024-05-29',3,0),(9,12,'00:15:06','2024-05-29',0,0),(10,35,'00:15:06','2024-05-29',1,0);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sudoku`
--

DROP TABLE IF EXISTS `sudoku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sudoku` (
  `id_sudoku` int NOT NULL,
  `difficulte` int NOT NULL,
  `case_init` longtext NOT NULL,
  PRIMARY KEY (`id_sudoku`),
  UNIQUE KEY `id_sudoku_UNIQUE` (`id_sudoku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sudoku`
--

LOCK TABLES `sudoku` WRITE;
/*!40000 ALTER TABLE `sudoku` DISABLE KEYS */;
INSERT INTO `sudoku` VALUES (0,6,'A3:5,A4:3,A6:9,A7:4,A9:7,B9:5,C3:4,C6:8,C9:6,D1:8,D3:2,D4:9,D5:3,D6:6,E2:3,E6:4,E8:5,F1:7,F3:1,F6:5,G4:5,G5:8,G6:2,G8:3,G9:9,H3:8,H6:3,H8:4,I2:9,I3:6,I4:4,I7:5,I9:8'),(1,12,'A3:5,A4:3,A6:9,A7:4,A9:7,B9:5,C3:4,C6:8,C9:6,D1:8,D3:2,D4:9,D5:3,D6:6,E2:3,E6:4,E8:5,F1:7,G9:9,H3:8,I9:8'),(2,8,'C3:4,C6:8,C9:6,D1:8,D3:2,D4:9,D5:3,D6:6,E2:3,E6:4,E8:5,F1:7,F3:1,F6:5,G4:5,G5:8,G6:2,G8:3,G9:9,H3:8,H6:3,H8:4,I2:9,I3:6,I4:4,I7:5,I9:8'),(3,20,'D8:9'),(4,15,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(5,2,'A3:5,A4:3,A6:9,A7:4,A9:7,B9:5,C3:4,C6:8,C9:6,D1:8,D3:2,D4:9,D5:3,D6:6,E2:3,E6:4,E8:5,F1:7,F3:1,F6:5,G4:5,G5:8,G6:2,G8:3,G9:9,H3:8,H6:3,H8:4,I2:9,I3:6,I4:4,I7:5,I9:8'),(6,5,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(7,8,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(8,8,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(9,15,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(10,11,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(11,2,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(12,1,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(13,18,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(14,9,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(15,7,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4'),(16,6,'D3:2,D4:9,D5:3,D6:6,E2:3,E6:4');
/*!40000 ALTER TABLE `sudoku` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-28 12:51:32
