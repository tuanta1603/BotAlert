-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th12 25, 2023 lúc 12:03 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `trading_api`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `bot_alert`
--

CREATE TABLE `bot_alert` (
  `id` int(11) NOT NULL,
  `syminfo` varchar(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  `ticker` varchar(255) DEFAULT NULL,
  `basecurrency` varchar(255) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `timeframe` varchar(255) DEFAULT NULL,
  `side` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `Action` varchar(255) DEFAULT NULL,
  `prices_pos` varchar(255) DEFAULT NULL,
  `prices_tp` varchar(255) DEFAULT NULL,
  `precent_tp` varchar(255) DEFAULT NULL,
  `pos_leverage` varchar(255) DEFAULT NULL,
  `pos_currency` varchar(255) DEFAULT NULL,
  `pos_quantity` varchar(255) DEFAULT NULL,
  `CurrencyManual` varchar(255) DEFAULT NULL,
  `QuantityManual` varchar(255) DEFAULT NULL,
  `codename` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `bot_alert`
--

INSERT INTO `bot_alert` (`id`, `syminfo`, `prefix`, `ticker`, `basecurrency`, `currency`, `timeframe`, `side`, `position`, `Action`, `prices_pos`, `prices_tp`, `precent_tp`, `pos_leverage`, `pos_currency`, `pos_quantity`, `CurrencyManual`, `QuantityManual`, `codename`, `type`) VALUES
(1, 'aaaaa', 'dddd', 'dddd', 'ddddd', 'aaaaaa', 'ffffff', 'gggggggg', 'sssssss', 'sssssssssssss', 'eeeeeeeeeeeee', 'rrrrrrrrrrrrrrrrrrrrr', 'rrrrrrrrrrrrrr', 'rrrrrrrrrrrrr', 'rrrrrrrrrrr', 'eeeeeeeeeeeeeeeeeeee', 'eeeeeeeeeeeeeeee', 'eeeeeeeeeeee', 'eeeeeeeeeeeeeee', 'wwwwwwwwwwwwwwwwwwwwwwww');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `bot_alert`
--
ALTER TABLE `bot_alert`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `bot_alert`
--
ALTER TABLE `bot_alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
