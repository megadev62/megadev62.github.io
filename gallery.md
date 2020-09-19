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

<body id="page-top">
    <!-- Navbar-->
    <nav class="navbar navbar-bg navbar-expand-lg navbar-dark sticky-top px-4 pt-3 pb-2">
        <div class="container-fluid">
            <a class="navbar-brand font-title" href="index.html">
                <img src="./assets/img/kab_bogor.png" alt="" loading="lazy">Desa Cilember
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end font-title" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Home<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="profil.html">Profil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="berita.html">Berita</a>
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
                    <li class="nav-item active">
                        <a class="nav-link" href="#page-top">Galeri</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#kontak">Kontak</a>
                    </li>
                </ul>
            </div>
        </div>

    </nav>
    <!-- container -->
    <div class="container my-5 gallery-pages">
        <div class="font-title title text-center">
            <span>Galeri Foto</span>
        </div>
        <div class="gallery-grid text-center">
            <div class="gallery-item pt-4 img-raised rounded">
                <a href="gallery-detail.html">
                    <img src="./assets/img/curug2.jpg" alt="" class="mb-3">
                    <p class="font-title">Curug</p>
                </a>
            </div>
            <div class="gallery-item pt-4 img-raised rounded">
                <a href="gallery-detail.html">
                    <img src="./assets/img/curug2.jpg" alt="" class="mb-3">
                    <p class="font-title">Curug</p>
                </a>
            </div>
            <div class="gallery-item pt-4 img-raised rounded">
                <a href="gallery-detail.html">
                    <img src="./assets/img/curug2.jpg" alt="" class="mb-3">
                    <p class="font-title">Curug</p>
                </a>
            </div>
            <div class="gallery-item pt-4 img-raised rounded">
                <a href="gallery-detail.html">
                    <img src="./assets/img/curug2.jpg" alt="" class="mb-3">
                    <p class="font-title">Curug</p>
                </a>
            </div>
            <div class="gallery-item pt-4 img-raised rounded">
                <a href="gallery-detail.html">
                    <img src="./assets/img/curug2.jpg" alt="" class="mb-3">
                    <p class="font-title">Curug</p>
                </a>
            </div>
        </div>
    </div>

    <!-- end container -->
    <footer class="text-light" id="kontak">
        <div class="container">
            <div class="row">
                <div class="col-md-4 col-xs-12">
                    <div class="row">
                        <div class="col font-sambung footer-brand">
                            <span>Desa</span><span class="text-warning">Cilember</span>
                        </div>
                    </div>
                    <div class="row no-gutters footer-icon mb-3">
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
                <div class="col-md-4 col-xs-12 my-auto">
                    <span class="text-warning">Alamat</span>
                    <p>Jl. Cilember No.104, Cilember, Kec. Cisarua, Bogor, Jawa Barat 16750</p>
                </div>
                <div class="col-md-4 col-xs-12 footer-layanan-masyarakat my-auto">
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
    <script src="./assets/js/scripts.js" type="text/javascript"></script>

</body>

</html>