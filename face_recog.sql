-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2020 at 02:38 PM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recog`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(10) NOT NULL,
  `name` varchar(80) NOT NULL,
  `id_number` int(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(30) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `type` int(1) NOT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `name`, `id_number`, `email`, `password`, `phone`, `type`, `status`) VALUES
(24, 'muhammad azeem', 50688, 'azeemmuhammad98@gmail.com', '1234', '08077401297', 1, 1),
(26, 'student1', 51688, 'student@gmail.com', '1234', '000000000', 0, 0),
(27, 'student2', 52688, 'student2@gmail.com', '1234', '000000000', 0, 0),
(28, 'student3', 53688, 'student3@gmail.com', '1234', '000000000', 0, 0),
(29, 'student4', 54688, 'student4@gmail.com', '1234', '000000000', 0, 0),
(30, 'Shivam', 50600, 'shivam@gmail.com', '1234', '08077401297', 0, 0),
(31, 'Siddahath', 50601, 'sidd@gmail.com', '1234', '08077401297', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(50) NOT NULL,
  `id_number` varchar(50) NOT NULL,
  `time1` varchar(50) NOT NULL,
  `date1` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `id_number`, `time1`, `date1`) VALUES
(1, '00000', '00:00:00', '2020-20-20'),
(3, '50688', '20:23:36', '2020-06-12'),
(5, '54688', '20:23:36', '2020-06-13'),
(6, '53688', '20:23:36', '2020-06-13'),
(7, '51688', '20:23:36', '2020-06-13'),
(8, '50600', '20:23:36', '2020-06-12'),
(9, '50601', '20:23:36', '2020-06-12'),
(10, '50600', '20:23:36', '2020-06-13'),
(67, '52688', '20:23:36', '2020-06-13'),
(76, '50688', '17:56:29', '2020-06-13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `id_number` (`id_number`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
