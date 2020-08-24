<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desa Cilember</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="./assets/font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>
    <!-- Navbar-->
    <div class="container-fluid">
        <nav class="navbar navbar-default navbar-expand-lg navbar-dark fixed-top px-4 pt-3 pb-2">
            <a class="navbar-brand font-title" href="#">
                <img src="./assets/img/kab_bogor.png" alt="" loading="lazy">Desa Cilember
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end font-weight-bolder" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Profil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Berita</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Layanan
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#">KTP</a>
                            <a class="dropdown-item" href="#">KK</a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Galeri</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Kontak</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
    <!-- end navbar -->
    <!-- video carousel -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <!-- The video -->
                <video autoplay muted loop id="myVideo">
                    <source src="./assets/video/vid5.mp4" type="video/mp4">
                </video>
                <!-- <div class="carousel-caption d-none d-md-block">
                    <h5>Curug 1</h5>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem ut commodi consequuntur
                        omnis fugit cumque assumenda sit distinctio, eveniet dignissimos voluptatem maxime consequatur
                        officiis adipisci natus odio. Eos, sequi consequatur?</p>
                </div> -->
            </div>
            <div class="carousel-item">
                <!-- The video -->
                <video autoplay muted loop id="myVideo">
                    <source src="./assets/video/vid6.mp4" type="video/mp4">
                </video>
                <!-- <div class="carousel-caption d-none d-md-block">
                    <h5>Curug 1</h5>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem ut commodi consequuntur
                        omnis fugit cumque assumenda sit distinctio, eveniet dignissimos voluptatem maxime consequatur
                        officiis adipisci natus odio. Eos, sequi consequatur?</p>
                </div> -->
            </div>
            <div class="carousel-item">
                <!-- The video -->
                <video autoplay muted loop id="myVideo">
                    <source src="./assets/video/vid4.mp4" type="video/mp4">
                </video>
                <!-- <div class="carousel-caption d-none d-md-block">
                    <h5>Curug 1</h5>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Exercitationem ut commodi consequuntur
                        omnis fugit cumque assumenda sit distinctio, eveniet dignissimos voluptatem maxime consequatur
                        officiis adipisci natus odio. Eos, sequi consequatur?</p>
                </div> -->
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
        <div class="welcome font-title">
            <span>Selamat Datang Di Website Desa Cilember</span><br>
            <p>Portal Berita dan Layanan Online Masyarkat</p>
        </div>
    </div>
    <!-- end video caraousel -->
    <!-- layanan nav -->
    <div class="container nav-layanan text-center">
        <!-- <div class="nav-layanan-title">
            <span class="font-title">Pelayanan Online</span>
        </div> -->
        <!-- <div class="container">
            <div class="row">
                <div class="col">
                    <div class="circle-icons bg-warning border rounded-circle">
                        <div class="layanan-icon">
                            <i class="fa fa-file-text-o" aria-hidden="true"></i>
                        </div>
                    </div>
                    <p class="mt-1">Pembuatan KTP</p>
                </div>
                <div class="col">
                    <div class="circle-icons badge-info border rounded-circle">
                        <div class="layanan-icon">
                            <i class="fa fa-file-text-o" aria-hidden="true"></i>
                        </div>
                    </div>
                    <p class="mt-1">Pembuatan KK</p>
                </div>
                <div class="col">
                    <div class="circle-icons badge-danger border rounded-circle">
                        <div class="layanan-icon">
                            <i class="fa fa-file-text-o" aria-hidden="true"></i>
                        </div>
                    </div>
                    <p class="mt-1">Pembuatan Surat</p>
                </div>
                <div class="col">
                    <div class="circle-icons bg-success border rounded-circle">
                        <div class="layanan-icon">
                            <i class="fa fa-file-text-o" aria-hidden="true"></i>
                        </div>
                    </div>
                    <p class="mt-1">Layanan Masyarkat</p>
                </div>
            </div>
        </div> -->

    </div>
    <!-- end layanan nav -->
    <!-- sambutan -->
    <div class="sambutan font-sambung">
        <div class="container text-center">
            <div class="row">
                <div class="col-4 my-auto">
                    <img src="./assets/img/default-avatar.png" alt="">
                    <p>Suhendi Hovenier</p>
                </div>
                <div class="col-8">
                    <div class="title">
                        <span>Sambutan Kepala Desa Cilember</span>
                    </div>
                    <p>"Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis
                        tenetur, nobis nemo sunt
                        pariatur, esse ea delectus labore, excepturi laborum repellendus illo amet vero animi porro
                        doloremque deserunt eius name."</p>
                </div>
            </div>
        </div>
    </div>
    <!-- end sambutan -->
    <!-- berita -->
    <div class="berita">
        <div class="container">
            <div class="font-title title">
                <span class="border-bt-2">Berita Terkini</span>
            </div>
            <div class="row">
                <div class="col-7 headline">
                    <img src="./assets/img/curug1.jpg" alt="">
                    <h5>Alam yang indah nan Sejuk</h5>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium odit molestias, et nam rerum
                        amet, repellendus ex animi a dolore voluptatum deleniti sit laboriosam soluta id modi eos cum?
                        Pariatur.</p>
                </div>
                <div class="col-5 side-bar">
                    <div class="row side-bar-news">
                        <div class="col-4"><img src="./assets/img/curug2.jpg" alt=""></div>
                        <div class="col-8 konten">
                            <h5>Alam yang indah nan Sejuk</h5>
                            <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet labore eius
                                reprehenderit sed? Consequuntur magnam numquam ad debitis vero id iure libero qui!
                                Omnis maiores iure et animi? Voluptates, necessitatibus.</span>
                        </div>
                    </div>
                    <div class="row side-bar-news">
                        <div class="col-4"><img src="./assets/img/curug2.jpg" alt=""></div>
                        <div class="col-8">
                            <h5>Alam yang indah nan Sejuk</h5>
                            <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet labore eius
                                reprehenderit sed? Consequuntur magnam numquam ad debitis vero id iure libero qui!
                                Omnis maiores iure et animi? Voluptates, necessitatibus.</span>
                        </div>
                    </div>
                    <div class="row side-bar-news">
                        <div class="col-4"><img src="./assets/img/curug2.jpg" alt=""></div>
                        <div class="col-8">
                            <h5>Alam yang indah nan Sejuk</h5>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet labore eius
                                reprehenderit sed? Consequuntur magnam numquam ad debitis vero id iure libero qui!
                                Omnis maiores iure et animi? Voluptates, necessitatibus.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- end berita -->
    <!-- struktur organisasi -->
    <div class="struktur">
        <div class="container">
            <div class="row">

            </div>
        </div>
    </div>
    <!-- end struktur organisasi -->
    <!-- galery -->
    <div class="galery text-center">
        <div class="container-fluid w-75">
            <div class="font-title title text-center">
                <span>Galeri Foto</span>
            </div>
            <div class="row">
                <div class="col-3 galery-box-img">
                    <a href=""> <img src="./assets/img/curug1.jpg" alt=""></a>
                </div>
                <div class="col-3 galery-box">
                    <div class="galery-title">
                        <a href="">
                            <span>Curug Cilember merupakan wisata populer dengan 7 air terjun di kawasan strategis
                                Puncak,
                                Bogor.</span>
                        </a>
                    </div>
                    <div class="date">
                        <span>5 Mei 2020</span>
                    </div>
                </div>
                <div class="col-3 galery-box-img">
                    <a href=""> <img src="./assets/img/curug1.jpg" alt=""></a>
                </div>
                <div class="col-3 galery-box">
                    <div class="galery-title">
                        <a href="">
                            <span>Curug Cilember merupakan wisata populer dengan 7 air terjun di kawasan strategis
                                Puncak,
                                Bogor.</span>
                        </a>
                    </div>
                    <div class="date">
                        <span>5 Mei 2020</span>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-3 galery-box">
                    <div class="galery-title">
                        <a href="">
                            <span>Curug Cilember merupakan wisata populer dengan 7 air terjun di kawasan strategis
                                Puncak,
                                Bogor.</span>
                        </a>
                    </div>
                    <div class="date">
                        <span>5 Mei 2020</span>
                    </div>
                </div>
                <div class="col-3 galery-box-img">
                    <a href=""> <img src="./assets/img/curug1.jpg" alt=""></a>
                </div>
                <div class="col-3 galery-box">
                    <div class="galery-title">
                        <a href="">
                            <span>Curug Cilember merupakan wisata populer dengan 7 air terjun di kawasan strategis
                                Puncak,
                                Bogor.</span>
                        </a>
                    </div>
                    <div class="date">
                        <span>5 Mei 2020</span>
                    </div>
                </div>
                <div class="col-3 galery-box-img">
                    <a href=""> <img src="./assets/img/curug1.jpg" alt=""></a>
                </div>
            </div>

            <div class="row text-center mt-5">
                <div class="col">
                    <button class="btn btn-info">Lebih Banyak</button>
                </div>
            </div>
        </div>
    </div>
    <!-- end galery -->
    <!-- footer -->
    <footer class="text-light">
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="row">
                        <div class="col font-sambung footer-brand">
                            <span>Desa</span><span class="text-warning">Cilember</span>
                        </div>
                    </div>
                    <div class="row no-gutters footer-icon">
                        <div class="col">
                            <a href=""> <i class="fa fa-facebook" aria-hidden="true"></i></a>
                        </div>
                        <div class="col">
                            <a href=""><i class="fa fa-twitter" aria-hidden="true"></i></a>
                        </div>
                        <div class="col">
                            <a href=""> <i class="fa fa-instagram" aria-hidden="true"></i></a>
                        </div>
                        <div class="col">
                            <a href=""> <i class="fa fa-envelope-o" aria-hidden="true"></i></a>
                        </div>
                        <div class="col">
                            <a href=""> <i class="fa fa-whatsapp" aria-hidden="true"></i></a>
                        </div>
                    </div>
                </div>
                <div class="col my-auto">
                    <span class="text-warning">Alamat</span>
                    <p>Jl. Cilember No.104, Cilember, Kec. Cisarua, Bogor, Jawa Barat 16750</p>
                </div>
                <div class="col footer-layanan-masyarakat my-auto">
                    <span class="text-warning">Layanan Masyarakat :</span><br>
                    <a href=""> Pembuatan KTP </a><br>
                    <a href=""> Pembuatan KK </a><br>
                    <a href=""> Pembuatan Surat-surat </a>
                </div>
            </div>
        </div>
    </footer>
    <!-- end footer -->
    <!--   Core JS Files   -->
    <script src="./assets/js/jquery.min.js" type="text/javascript"></script>
    <script src="./assets/js/popper.min.js" type="text/javascript"></script>
    <script src="./assets/js/bootstrap.min.js" type="text/javascript"></script>
    <script src="./assets/slick/slick.min.js" type="text/javascript"></script>

    <script src="./assets/js/scripts.js" type="text/javascript"></script>
</body>

</html>
