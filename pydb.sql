-- MariaDB dump 10.19  Distrib 10.5.26-MariaDB, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------

USE test;

--
-- Table structure for table `essay`
--

DROP TABLE IF EXISTS `essay`;
CREATE TABLE `essay` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` char(50) DEFAULT NULL,
  `data` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `essay`
--

LOCK TABLES `essay` WRITE;
INSERT INTO `essay` VALUES (1,'Person A','A hash function is any function that can be used to map data of arbitrary size to fixed-size values, though there are some hash functions that support variable-length output. The values returned by a hash function are called hash values, hash codes, hash digests, digests, or simply hashes. The value are usually used to index a fixed-size table called a hash table. Use of a hash function to index a hash table is called hashing or scatter-storage addressing.\n'),(2,'Person B','The values returned by a hash function are called hash values, hash codes, hash digests, digests, or simply hashes. \nThe value are usually used to index a fixed-size table called a hash table.\nUse of a hash function to index a hash table is called hashing or scatter-storage addressing.\nA hash function is any function that can be used to map data of arbitrary size to fixed-size values, \nthough there are some hash functions that support variable-length output.');
UNLOCK TABLES;

-- Dump completed on 2024-12-31 00:00:00
