-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Mag 11, 2020 alle 23:41
-- Versione del server: 10.3.22-MariaDB-0+deb10u1
-- Versione PHP: 7.3.14-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dnd_5_weapons`
--

DELIMITER $$
--
-- Procedure
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `getWeaponsByCategory` (IN `input_category` VARCHAR(1000) CHARSET armscii8)  NO SQL
BEGIN

SELECT Category,Name,Damages,Combat FROM weapons WHERE Category like CONCAT('%',input_category,'%') ORDER BY Name;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getWeaponsByName` (IN `input_name` VARCHAR(1000) CHARSET armscii8)  NO SQL
BEGIN
	SELECT * FROM weapons WHERE Name like CONCAT('%', input_name , '%') GROUP BY Name;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Struttura della tabella `weapons`
--

CREATE TABLE `weapons` (
  `Name` varchar(500) NOT NULL,
  `Category` varchar(300) NOT NULL,
  `Combat` varchar(300) NOT NULL,
  `Cost` text NOT NULL,
  `Damages` text NOT NULL,
  `Properties` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `weapons`
--

INSERT INTO `weapons` (`Name`, `Category`, `Combat`, `Cost`, `Damages`, `Properties`) VALUES
('Alabarda', 'Arma da guerra', 'da mischia', '20 mo ', '1d10 taglienti', '3kg , Due mani , Pesante , portata'),
('Arco corto', 'Arma semplice', 'da distanza', '25 mo', '1d6 perforanti', 'Due mani,1kg,Munizioni (gittata 24/96m)'),
('Arco lungo', 'Arma da guerra', 'da distanza', '50 mo', '1d8 perforanti', '1 Kg, Due Mani, Munizioni (gittata 45/180m),Pesante'),
('Ascia', 'Arma semplice', 'da mischia', '5 mo', '1d6 taglienti', 'da lancio (con gittata 6/18m) , leggera 1kg'),
('Ascia Bipenne', 'Arma da guerra', 'da mischia', '30 m0 ', '1d12 taglienti', '3,5 kg,Due mani,Pesante'),
('Ascia da battaglia', 'Arma da guerra', 'da mischia', '10 m0', '1d8 taglienti', '2kg , Versatile(1d10)'),
('Balestra a mano', 'Arma da guerra', 'da distanza', '75 mo', '1d6 perforanti', '1,5 kg, Leggera, Munizioni (gittata 9/36m), Ricarica'),
('Balestra leggera', 'Arma semplice', 'da distanza', '25 mo', '1d8 perforanti', 'Due mani 2,5kg , Munizioni (gittata 24/96m), Ricarica'),
('Balestra Pesante', 'Arma da guerra', 'da distanza', '50 mo', '1d10 perforanti', '9 Kg , Due mani, munizioni (gittata 30/120m), Pesante , Ricarica'),
('Bastone Ferrato', 'Arma semplice', 'da mischia', '2 ma', '1d6 contundenti', 'Versatile (1d8),2 kg'),
('Cerbottana', 'Arma da guerra', 'da distanza', '10 m0', '1 perforante\r\n', '0,5 kg,Munizioni (gittata 7,5/30m),Ricarica'),
('Dardo', 'Arma semplice', 'da distanza', '5 mr', '1d4 perforanti', '0,125kg,Accurata,lancio(gittata 6/18m)'),
('Falcetto', 'Arma semplice', 'da mischia', '1 mo', '1d4 taglienti', 'Leggera,1kg'),
('Falcione', 'Arma da guerra', 'da mischia', '20 m0 ', '1d10 taglienti', '3kg,Due mani,Pesante,Portata'),
('Fionda', 'Arma semplice', 'da distanza', '1 ma', '1d4 contundenti', 'Munizioni (gittata 9/36m)'),
('Frusta', 'Arma da guerra', 'da mischia', '2 m0', '1d4 taglienti', '1,5kg,Accurata,Portata'),
('Giavellotto', 'Arma semplice ', 'da mischia', '5 ma', '1d6 perforanti', 'da lancio con gittata(9/36m)'),
('Lancia', 'Arma semplice', 'da mischia', '1 mo', '1d6 perforanti', 'Lancio (con gittata 6/18m),Leggera 1,5kg'),
('Lancia da cavaliere', 'Arma da guerra', 'da mischia', '10 m0', '1d12 perforanti', '3 kg,Portata,Speciale'),
('Maglio', 'Arma da guerra', 'da mischia', '10 mo', '2d6 contundenti', '5 kg,Due mani,Pesante'),
('Martello da guerra', 'Arma da guerra', 'da mischia', '15 mo', '1d8 contundenti', '1 kg,Versatile (1d10)'),
('Martello leggero', 'Arma semplice', 'da mischia', '2 mo', '1d4 contundenti', 'Lancio (con gittata 6/18m),Versatile (1d8)'),
('Mazza', 'Arma semplice', 'da mischia', '5 mo', '1d6 contundenti', '2 kg'),
('Mazzafrusto', 'Arma da guerra', 'da mischia', '10 mo', '1d8 contundenti', '1 kg'),
('Morning star', 'Arma da guerra', 'da mischia', '15 m0', '1d8 perforanti', '2 kg'),
('Picca', 'Arma da guerra', 'da mischia', '5 m0', '1d10 perforanti', 'Due mani,9 kg,Pesante,Portata'),
('Piccone da guerra', 'Arma da guerra', 'da mischia', '5 mo', '1d8 perforanti\r\n', '1 kg'),
('Pugnale', 'Arma semplice', 'da mischia', '2 mo', '1d4 taglienti', 'Accurata\r\nDa lancio (gittata 6/18m)\r\nLeggera 0,5kg'),
('Randello', 'Arma semplice ', 'da mischia', '1 ma', '1d4 contundenti', 'Leggera 1kg'),
('Randello Pesante', 'Arma semplice', 'da mischia', '2 ma', '1d8 contundenti', 'A due mani,5 kg'),
('Rete', 'Armi da guerra', 'da distanza', '1 mo', 'Non specificati', 'Lancio (gittata 1,5/4,5m),Speciale'),
('Scimitarra', 'Arma da guerra', 'da mischia', '25 mo', '1d6 taglienti', '1,5 kg ,Accurata,Leggera'),
('Spada corta', 'Arma da guerra', 'da mischia', '10 mo', '1d6 perforanti', '1 kg \r\nAccurata\r\nleggera'),
('Spada lunga', 'Arma da guerra', 'da mischia', '15 m0', '1d8 taglienti', '1,5 kg,Versatile (1d10)'),
('Spadone', 'Arma da guerra', 'da mischia', '50 m0', '2d6 taglienti', '3 Kg,Due mani,Pesante'),
('Stocco', 'Arma da guerra', 'da mischia', '25 mo', '1d8 perforanti', 'Accurata'),
('Tridente', 'Arma da guerra', 'da mischia', '5 mo', '1d6 perforanti', 'Lancio (gittata 6/18m),Versatile (1d8)');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `weapons`
--
ALTER TABLE `weapons`
  ADD PRIMARY KEY (`Name`),
  ADD UNIQUE KEY `Nome` (`Name`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
