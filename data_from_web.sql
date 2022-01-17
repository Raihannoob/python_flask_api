-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 17, 2022 at 05:39 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Scrap`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_from_web`
--

CREATE TABLE `data_from_web` (
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `ratting` varchar(255) NOT NULL,
  `prices` int(255) NOT NULL,
  `Amenities` varchar(255) NOT NULL,
  `images` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_from_web`
--

INSERT INTO `data_from_web` (`name`, `location`, `ratting`, `prices`, `Amenities`, `images`) VALUES
('The Park Hyderabad', 'Hyderabad,Somajiguda', '5.9', 68, 'Parking Pool Spa', 'https://content.r9cdn.net/rimg/himg/03/ae/24/ice-233787598-70639058_3XL-345367.jpg?width=335&height=268&crop=true'),
('Taj Falaknuma Palace', 'Hyderabad', '9.5', 674, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/rimg/himg/a7/cb/c3/leonardo-1200539-Ladies_Room_O-406516.jpg?width=335&height=268&crop=true'),
('Radisson Blu Plaza Hotel Hyderabad Banjara Hills', 'Hyderabad,Banjara Hills', '8.1', 143, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/63/f4/d2/ice-114052-68261612_3XL-183398.jpg'),
('Vivanta Hyderabad, Begumpet', 'Hyderabad,Begumpet', '8.4', 88, 'Parking Free Wi-Fi Pool Pet-friendly', 'https://content.r9cdn.net/himg/3c/d2/17/leonardo-1265626-Premium_Temptation_Room_O-762499.jpg'),
('Taj Deccan', 'Hyderabad,Banjara Hills', '8.4', 92, 'Parking Free Wi-Fi Pool', 'https://content.r9cdn.net/himg/9f/15/59/revato-174753-12755053-295730.jpg'),
('Novotel Hyderabad Airport', 'Hyderabad', '7.3', 103, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/b6/3f/62/ice-38052-79062133_3XL-062407.jpg'),
('Sheraton Hyderabad Hotel', 'Hyderabad', '8.8', 134, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/75/c9/e3/leonardo-2009194-hydsi-lobby-9337-hor-clsc_O-600874.jpg'),
('ITC Kakatiya, a Luxury Collection Hotel, Hyderabad', 'Hyderabad,Begumpet', '7.8', 125, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/0f/d2/92/leonardo-1124231-hydlc-exterior-6031-hor-clsc_O-655062.jpg'),
('Taj Banjara', 'Hyderabad,Banjara Hills', '7.7', 64, 'Parking Free Wi-Fi Pool Pet-friendly', 'https://content.r9cdn.net/himg/18/92/8d/leonardo-1124423-Underdeck_O-051747.jpg'),
('The Westin Hyderabad Mindspace', 'Hyderabad,Madhapur', '8.5', 149, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/b3/19/03/leonardo-125231038-hydwi-hyderabad-6067-hor-clsc_O-780326.jpg'),
('Taj Krishna', 'Hyderabad,Banjara Hills', '8.2', 126, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/9f/8c/f4/leonardo-2671001-Luxury_Suite_O-859481.jpg'),
('Lemon Tree Premier, Hitec City, Hyderabad', 'Hyderabad,HITEC City', '7.5', 95, 'Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/db/69/23/leonardo-1233630-6.35.01.01_Facade_O-039005.jpg'),
('Oakwood Residence Kapil Hyderabad', 'Hyderabad', '8.7', 69, 'Parking Free Wi-Fi Pool Pet-friendly', 'https://content.r9cdn.net/himg/23/b6/43/revato-893414-11732064-124166.jpg'),
('The Golkonda Hyderabad', 'Hyderabad', '7.2', 59, 'Parking Free Wi-Fi Pool', 'https://content.r9cdn.net/himg/81/99/1e/leonardo-196301398-Jewel_Of_Nizam_Entrance_CF_O-674724.jpg'),
('Radisson Hyderabad Hitec City', 'Hyderabad,Gachibowli', '6.8', 108, 'Parking Free Wi-Fi Pool', 'https://content.r9cdn.net/himg/f5/3b/72/ice-114077-63658134_3XL-413941.jpg'),
('Hyatt Hyderabad Gachibowli', 'Hyderabad', '7.8', 129, 'Parking Free Wi-Fi Pool Pet-friendly', 'https://content.r9cdn.net/himg/c5/94/45/ice-49838-61030212_3XL-980957.jpg'),
('Park Hyatt Hyderabad', 'Hyderabad,Jubilee Hills', '8.1', 128, 'Parking Pool Spa', 'https://content.r9cdn.net/rimg/himg/6b/ac/80/ice-49839-63963623_3XL-093595.jpg?width=335&height=268&crop=true'),
('Trident Hyderabad', 'Hyderabad,HITEC City', '9.2', 138, 'Parking Pool Spa', 'https://content.r9cdn.net/rimg/himg/77/09/84/leonardo-1272069-010-Trident_Hyderabad-Amara_O-247227.jpg?width=335&height=268&crop=true'),
('Novotel Hyderabad Convention Centre', 'Hyderabad', '7.8', 113, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/8b/b2/2f/leonardo-116684774-6182_rsr001_05_p_3000x2250_O-622254.jpg'),
('Itc Kohenur, A Luxury Collection Hotel, Hyderabad', 'Hyderabad,Madhapur', '8.2', 158, 'Parking Free Wi-Fi Pool Spa', 'https://content.r9cdn.net/himg/8b/b2/2f/leonardo-116684774-6182_rsr001_05_p_3000x2250_O-622254.jpg');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
