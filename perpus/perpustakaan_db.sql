-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2025 at 07:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `id` int(11) NOT NULL,
  `kode_anggota` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `alamat` text NOT NULL,
  `telepon` varchar(15) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`id`, `kode_anggota`, `nama`, `alamat`, `telepon`, `email`, `created_at`) VALUES
(1, 'A01', 'Tika', 'bontang', '812345678', 'tika@gmail.com', '2025-10-22 05:05:17');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `kode_buku` varchar(20) NOT NULL,
  `judul` varchar(200) NOT NULL,
  `pengarang` varchar(100) NOT NULL,
  `penerbit` varchar(100) NOT NULL,
  `tahun_terbit` int(11) NOT NULL,
  `stok` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id`, `kode_buku`, `judul`, `pengarang`, `penerbit`, `tahun_terbit`, `stok`, `created_at`) VALUES
(3, 'B001', 'Delisa', 'Tere Liye', 'Tere Liye', 2004, 10, '2025-10-22 05:26:10'),
(4, 'B002', 'Negeri Para Bedebah', 'Tere Liye', 'Gramedia', 2012, 15, '2025-10-22 05:26:10'),
(5, 'B003', 'Laskar Pelangi', 'Andrea Hirata', 'Bentang Pustaka', 2005, 20, '2025-10-22 05:26:10'),
(6, 'B004', 'Sang Pemimpi', 'Andrea Hirata', 'Bentang Pustaka', 2006, 18, '2025-10-22 05:26:10'),
(7, 'B005', 'Edensor', 'Andrea Hirata', 'Bentang Pustaka', 2007, 15, '2025-10-22 05:26:10'),
(8, 'B006', 'Cinta Brontosaurus', 'Raditya Dika', 'GagasMedia', 2006, 12, '2025-10-22 05:26:10'),
(9, 'B007', 'Koala Kumal', 'Raditya Dika', 'GagasMedia', 2015, 10, '2025-10-22 05:26:10'),
(10, 'B008', 'Manusia Setengah Salmon', 'Raditya Dika', 'GagasMedia', 2011, 9, '2025-10-22 05:26:10'),
(11, 'B009', 'Dilan 1990', 'Pidi Baiq', 'Pastel Books', 2014, 25, '2025-10-22 05:26:10'),
(12, 'B010', 'Dilan 1991', 'Pidi Baiq', 'Pastel Books', 2015, 22, '2025-10-22 05:26:10'),
(13, 'B011', 'Milea: Suara dari Dilan', 'Pidi Baiq', 'Pastel Books', 2016, 18, '2025-10-22 05:26:10'),
(14, 'B012', 'Filosofi Kopi', 'Dewi Lestari', 'Bentang Pustaka', 2006, 14, '2025-10-22 05:26:10'),
(15, 'B013', 'Perahu Kertas', 'Dewi Lestari', 'Bentang Pustaka', 2008, 16, '2025-10-22 05:26:10'),
(16, 'B014', 'Supernova: Ksatria, Puteri, dan Bintang Jatuh', 'Dewi Lestari', 'Truedee Books', 2001, 10, '2025-10-22 05:26:10'),
(17, 'B015', '5 CM', 'Donny Dhirgantoro', 'Grasindo', 2005, 20, '2025-10-22 05:26:10'),
(18, 'B016', 'Bumi', 'Tere Liye', 'Gramedia', 2014, 30, '2025-10-22 05:26:10'),
(19, 'B017', 'Bulan', 'Tere Liye', 'Gramedia', 2015, 25, '2025-10-22 05:26:10'),
(20, 'B018', 'Matahari', 'Tere Liye', 'Gramedia', 2016, 24, '2025-10-22 05:26:10'),
(21, 'B019', 'Hujan', 'Tere Liye', 'Gramedia', 2016, 28, '2025-10-22 05:26:10'),
(22, 'B020', 'Pulang', 'Tere Liye', 'Gramedia', 2015, 22, '2025-10-22 05:26:10'),
(23, 'B021', 'Pergi', 'Tere Liye', 'Gramedia', 2018, 20, '2025-10-22 05:26:10'),
(24, 'B022', 'Tentang Kamu', 'Tere Liye', 'Gramedia', 2016, 25, '2025-10-22 05:26:10'),
(25, 'B023', 'Rindu', 'Tere Liye', 'Republika', 2014, 18, '2025-10-22 05:26:10'),
(26, 'B024', 'Ayah Aku Berbeda', 'Tere Liye', 'Republika', 2010, 15, '2025-10-22 05:26:10'),
(27, 'B025', 'Anak Semua Bangsa', 'Pramoedya Ananta Toer', 'Lentera Dipantara', 1981, 10, '2025-10-22 05:26:10');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` enum('admin','petugas') DEFAULT 'petugas',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `created_at`) VALUES
(1, 'admin', 'admin123', 'admin', '2025-10-20 07:26:04'),
(2, 'taro', '12345', 'petugas', '2025-10-20 07:38:20'),
(3, 'bram', '123456789', 'petugas', '2025-10-22 05:03:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_anggota` (`kode_anggota`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_buku` (`kode_buku`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
