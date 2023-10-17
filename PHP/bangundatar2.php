<?php
class BangunDatar {
    var $luas;
    var $keliling;
    var $jenis;

    public function __construct($luas, $keliling, $jenis) {
        $this->luas = $luas;
        $this->keliling = $keliling;
        $this->jenis = $jenis;
    }

    public function hitungLuas() {
        return $this->luas;
    }

    public function hitungKeliling() {
        return $this->keliling;
    }

    public function getJenis() {
        return $this->jenis;
    }
}

class Persegi extends BangunDatar {
    private $sisi;

    public function __construct($sisi) {
        $this->sisi = $sisi;
    }

    public function hitungLuas() {
        $this->luas = $this->sisi * $this->sisi;
        return $this->luas;
    }

    public function hitungKeliling()
    {
        $this->keliling = 4 * $this->sisi;
        return $this->keliling;
    }
}

class PersegiPanjang extends BangunDatar {
    private $panjang;
    private $lebar;

    public function __construct($panjang, $lebar) {
        
        $this->panjang = $panjang;
        $this->lebar = $lebar;
    }

    public function hitungLuas() {
        $this->luas = $this->panjang * $this->lebar;
        return $this->luas;
    }

    public function hitungKeliling()
    {
        $this->keliling = 2 * ($this->panjang + $this->lebar);
        return $this->keliling;
    }
}

class Segitiga extends BangunDatar {
    private $sisi1;
    private $sisi2;
    private $sisi3;
    private $alas;
    private $tinggi;

    public function __construct($sisi1, $sisi2, $sisi3, $alas, $tinggi) {
        
        $this->sisi1 = $sisi1;
        $this->sisi2 = $sisi2;
        $this->sisi3 = $sisi3;
        $this->alas = $alas;
        $this->tinggi = $tinggi;
    }

    public function hitungLuas() {
        $this->luas = 0.5 * $this->alas * $this->tinggi;
        return $this->luas;
    }

    public function hitungKeliling() {
        $this->keliling = $this->sisi1 + $this->sisi2 + $this->sisi3;
        return $this->keliling;
    }
}

class Lingkaran extends BangunDatar {
    private $jarijari;

    public function __construct($jarijari) {
        
        $this->jarijari = $jarijari;
    }

    public function hitungLuas()
    {
        $this->luas = 3.14 * $this->jarijari * $this->jarijari;
        return $this->luas;
    }

    public function hitungKeliling()
    {
        $this->keliling = 2 * 3.14 * $this->jarijari;
        return $this->keliling;
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $jenis_bangun_datar = $_POST["jenis_bangun_datar"];

    switch ($jenis_bangun_datar) {
        case "persegi" :
            $sisi = $_POST["sisi_persegi"];
            $bangunDatar = new Persegi($sisi);
            $luas = $bangunDatar->hitungLuas();
            $keliling = $bangunDatar->hitungKeliling();
            $jenis = $bangunDatar->getJenis();
            break;

        case "persegi_panjang" :
            $panjang = $_POST["panjang_persegi_panjang"];
            $lebar = $_POST["lebar_persegi_panjang"];
            $bangunDatar = new PersegiPanjang($panjang, $lebar);
            $luas = $bangunDatar->hitungLuas();
            $keliling = $bangunDatar->hitungKeliling();
            $jenis = $bangunDatar->getJenis();
            break;
        case "segitiga" :
            $sisi1 = $_POST["sisi1_segitiga"];
            $sisi2 = $_POST["sisi2_segitiga"];
            $sisi3 = $_POST["sisi3_segitiga"];
            $alas = $_POST["alas_segitiga"];
            $tinggi = $_POST["tinggi_segitiga"];
            $bangunDatar = new Segitiga($sisi1, $sisi2, $sisi3, $alas, $tinggi);
            $luas = $bangunDatar->hitungLuas();
            $keliling = $bangunDatar->hitungKeliling();
            $jenis = $bangunDatar->getJenis();
            break;
    
        case "lingkaran" :
            $jarijari = $_POST["jarijari_lingkaran"];
            $bangunDatar = new Lingkaran($jarijari);
            $luas = $bangunDatar->hitungLuas();
            $keliling = $bangunDatar->hitungKeliling();
            $jenis = $bangunDatar->getJenis();
            break;

        default :
            $bangunDatar = null;
            break;
        }
}
?>
        
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Bangun Datar</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 20px;
        }

        h1 {
            color: #010101;
            text-align: center;
        }
        
        h4 {
            color: #010101;
            text-align: center;
            font-weight: 100;
            font-style: italic;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
        }

        select {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            align-items: center;
            background-color: #007BFF;
            color: #fff;
            cursor: pointer;
            border-radius: 10px;
            padding: 8px;
            width: 50%;
            display: block;
            margin: 0 auto;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
            transform: scale(1.1);
        }

        #hasil {
            margin-top: 50px;
            align-content: center;
        }

        #hasil h2 {
            text-align: center;
        }

        #hasil p {
            margin-bottom: 8px;
            text-align: center;
        }
    </style>
</head>

<body>
    <h1>Kalkulator Bangun Datar</h1>
    <h4>Menghitung luas dan keliling bangun datar</h4>
    <br>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="jenis_bangun_datar">Pilih Jenis Bangun Datar : </label>
        <select name="jenis_bangun_datar" id="jenis_bangun_datar">
            <option value="persegi">Persegi</option>
            <option value="persegi_panjang">Persegi Panjang</option>
            <option value="segitiga">Segitiga</option>
            <option value="lingkaran">Lingkaran</option>
        </select>
        <br><br>

        <div id="input_persegi" style="display: none;">
            <label for="sisi_persegi">Sisi Persegi:</label>
            <input type="text" name="sisi_persegi" value="0" required>
        </div>
        <br>

        <div id="input_persegi_panjang" style="display: none;">
            <label for="panjang_persegi_panjang">Panjang Persegi Panjang:</label>
            <input type="text" name="panjang_persegi_panjang" value="0" required> <br>
            <label for="lebar_persegi_panjang">Lebar Persegi Panjang:</label>
            <input type="text" name="lebar_persegi_panjang" value="0" required><br>
        </div>


        <div id="input_segitiga" style="display: none;">
            <label for="sisi1_segitiga">Sisi 1 Segitiga:</label>
            <input type="text" name="sisi1_segitiga" value="0" required> <br>
            <label for="sisi2_segitiga">Sisi 2 Segitiga:</label>
            <input type="text" name="sisi2_segitiga" value="0" required> <br>
            <label for="sisi3_segitiga">Sisi 3 Segitiga:</label>
            <input type="text" name="sisi3_segitiga" value="0" required> <br>
            <label for="alas_segitiga">Alas Segitiga:</label>
            <input type="text" name="alas_segitiga" value="0" required> <br>
            <label for="tinggi_segitiga">Tinggi Segitiga:</label>
            <input type="text" name="tinggi_segitiga" value="0" required> <br>
        </div>

        <div id="input_lingkaran" style="display: none;">
        <label for="jarijari_lingkaran">Jari-jari Lingkaran:</label>
        <input type="text" name="jarijari_lingkaran" value="0" required> <br>
        </div>

        <br>
        <input type="submit" value="Hitung">
    </form>

    <?php if ($_SERVER["REQUEST_METHOD"] == "POST"): ?>
    <div id="hasil">
        <h2>Hasil Perhitungan</h2>
        <?php if ($bangunDatar instanceof BangunDatar): ?>
            <p>Jenis Bangun Datar: <?php echo $jenis_bangun_datar . "<br>";; ?></p>
            <p>Luas: <?php echo isset($luas) ? $luas : '0'; ?></p>
            <p>Keliling: <?php echo isset($keliling) ? $keliling : '0'; ?></p>
        <?php else: ?>
            <p>Masukkan parameter yang valid untuk menghitung.</p>
        <?php endif; ?>
    </div>
    <?php endif; ?>

    <script>
    // Menampilkan input sesuai dengan jenis bangun datar yang dipilih
    document.getElementById("jenis_bangun_datar").addEventListener("change", function () {
        var selectedBangun = this.value;
        var inputDivs = document.querySelectorAll("[id^='input_']");

        inputDivs.forEach(function (div) {
            div.style.display = "none";
        });

        document.getElementById("input_" + selectedBangun).style.display = "block";
    });

    // Memanggil fungsi secara otomatis saat halaman dimuat untuk menetapkan tampilan awal
    document.addEventListener("DOMContentLoaded", function() {
        var selectedBangun = document.getElementById("jenis_bangun_datar").value;
        var inputDivs = document.querySelectorAll("[id^='input_']");

        inputDivs.forEach(function (div) {
            div.style.display = "none";
        });

        document.getElementById("input_" + selectedBangun).style.display = "block";
    });
    </script>
</body>
</html>