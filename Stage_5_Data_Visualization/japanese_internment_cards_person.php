<!DOCTYPE HTML>
<!--
        ZeroFour by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<?php
$row = 1;
if (($handle = fopen("complete_data.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 10000, ",")) !== FALSE) {
        $num = count($data);
        $id = $_GET['id'];
        if ($data[0] == $id) {
            $content = $data;
        }
    }
}
?>
<html>
    <head>
        <title>Japanese occupation of the Dutch East Indie</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="assets/css/main.css" />
        <style>
            .header_person {
                margin-left: 150px;
                margin-right: 150px;
                margin-top: -10px;
                padding-top: 0.5px;
                padding-bottom: 0.2em;
                margin-bottom: 10px;
            }

            .header_person2 {
                margin-top: -15px;
            }

            .person_info {
                margin-left: 150px;
                margin-right: 150px;
                padding-left: 40px;
                padding-right: 40px;
            }

            .button_information {
                display: inline-block;
                border-radius: 4px;
                background-color: #212932;
                border: none;
                color: #FFFFFF;
                text-align: center;
                font-size: 15px;
                padding: 10px;
                width: 340px;
                transition: all 0.5s;
                cursor: pointer;
                margin: 15px 0px -40px 29em;
            }

            .button_information span {
                cursor: pointer;
                display: inline-block;
                position: relative;
                transition: 0.5s;
            }

            .button_information span:after {
                content: '\00bb';
                position: absolute;
                opacity: 0;
                top: 0;
                right: -20px;
                transition: 0.5s;
            }

            .button_information:hover span {
                padding-right: 25px;
            }

            .button_information:hover span:after {
                opacity: 1;
                right: 0;
            }

            .button_information:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
                background-color: #E7E7E7;
            }
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script>
            $(document).ready(function () {
                $('.to_hide_show').hide();
                var count = 0;

                $(".button_information").click(function () {
                    count++;
                    count % 2 ? $firstFunction() : $secondFunction();
                });

                function $firstFunction() {
                    $(".information_text").html("Show less information");
                    $('.to_hide_show').show();
                }
                function $secondFunction() {
                    $(".information_text").html("Show more information");
                    $('.to_hide_show').hide();
                }
            });
        </script>
    </head>
    <body class="no-sidebar is-preload">
        <div id="page-wrapper">
            <div id="header-wrapper">
                <div class="container">
                    <header id="header">
                        <div class="inner">
                            <h1><a href="index.php" id="logo">Second World War</a></h1>
                            <nav id="nav">
                                <ul>
                                    <li><a href="index.php">Home</a></li>
                                    <li class="current_page_item"><a href="japanese_internment_cards.php">JAPANESE INTERNMENT CARDS</a></li>
                                </ul>
                            </nav>
                        </div>
                    </header>
                </div>
            </div>

            <div id="main-wrapper">
                <div class="wrapper style2">
                    <div class="inner">
                        <div class="container">
                            <div id="content">
                                <article>
                                    <header class="major" style="text-align:center;">
                                        <h2><?php echo $content[1]; ?></h2>
                                    </header>
                                    <?php
                                    if ($content[5] != "" || $content[40] != "") {
                                        ?>
                                        <div class="wrapper style3 header_person">
                                            <div class="inner">
                                                <div class="container header_person2">
                                                    <h3>Birth</h3>
                                                </div>
                                            </div>
                                        </div>
                                        <p class="person_info">
                                            <?php
                                            if ($content[5] != "") {
                                                ?>
                                                <strong>Date: </strong><?php echo $content[5]; ?>
                                                <?php
                                            }
                                            if ($content[5] != "" && $content[40] != "") {
                                                echo "<br>";
                                            }
                                            if ($content[40] != "") {
                                                ?>
                                                <strong>Place: </strong><?php echo ucfirst($content[40]); ?>
                                            <?php } ?>
                                        </p>
                                        <?php
                                    }
                                    if ($content[37] != "" || $content[41] != "") {
                                        ?>
                                        <div class="wrapper style3 header_person">
                                            <div class="inner">
                                                <div class="container header_person2">
                                                    <h3>Death</h3>
                                                </div>
                                            </div>
                                        </div>
                                        <p class="person_info">
                                            <?php
                                            if ($content[37] != "") {
                                                ?>
                                                <strong>Date: </strong><?php echo $content[37]; ?>
                                                <?php
                                            }
                                            if ($content[37] != "" && $content[41] != "") {
                                                echo "<br>";
                                            }
                                            if ($content[41] != "") {
                                                ?>
                                                <strong>Place: </strong><?php echo ucfirst($content[41]); ?>
                                            <?php } ?>
                                        </p>
                                        <?php
                                    }
                                    if ($content[11] != "" || $content[10] != "" || $content[18] != "" || $content[19] != "" || $content[20] != "" || $content[21] != "" || $content[22] != "" || $content[23] != "" || $content[24] != "" || $content[25] != "" || $content[26] != "" || $content[27] != "" || $content[28] != "" || $content[29] != "" || $content[30] != "") {
                                        ?>
                                        <div class="wrapper style3 header_person">
                                            <div class="inner">
                                                <div class="container header_person2">
                                                    <h3>Capture</h3>
                                                </div>
                                            </div>
                                        </div>
                                        <p class="person_info">
                                            <?php
                                            if ($content[11] != "") {
                                                ?>
                                                <strong>Date: </strong><?php echo $content[11]; ?> <br>
                                                <?php
                                            }
                                            if ($content[10] != "") {
                                                ?>
                                                <strong>Place: </strong><?php echo ucfirst($content[10]); ?> <br>
                                                <?php
                                            }
                                            if ($content[18] != "" || $content[19] != "" || $content[20] != "" || $content[21] != "" || $content[22] != "") {
                                                ?>
                                                <strong>Camp and transfer date: </strong> <br>
                                                <?php
                                                if ($content[18] != "") {
                                                    echo "&#8226;  " . ucfirst($content[18]);
                                                }
                                                if ($content[18] != "" && $content[19] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[19] != "") {
                                                    echo "&#8226;  " . ucfirst($content[19]);
                                                }
                                                if (($content[18] != "" || $content[19] != "") && $content[20] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[20] != "") {
                                                    echo "&#8226;  " . ucfirst($content[20]);
                                                }
                                                if (($content[18] != "" || $content[19] != "" || $content[20] != "") && $content[21] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[21] != "") {
                                                    echo "&#8226;  " . ucfirst($content[21]);
                                                }
                                                if (($content[18] != "" || $content[19] != "" || $content[20] != "" || $content[21] != "") && $content[22] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[22] != "") {
                                                    echo "&#8226;  " . ucfirst($content[22]);
                                                }
                                                echo "<br>";
                                            }
                                            if ($content[23] != "" || $content[24] != "" || $content[25] != "" || $content[26] != "" || $content[27] != "") {
                                                ?>
                                                <strong>Camp branch name and registration number: </strong> <br>
                                                <?php
                                                if ($content[23] != "") {
                                                    echo "&#8226;  " . ucfirst($content[23]);
                                                }
                                                if ($content[23] != "" && $content[24] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[24] != "") {
                                                    echo "&#8226;  " . ucfirst($content[24]);
                                                }
                                                if (($content[23] != "" || $content[24] != "") && $content[25] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[25] != "") {
                                                    echo "&#8226;  " . ucfirst($content[25]);
                                                }
                                                if (($content[23] != "" || $content[24] != "" || $content[25] != "") && $content[26] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[26] != "") {
                                                    echo "&#8226;  " . ucfirst($content[26]);
                                                }
                                                if (($content[23] != "" || $content[24] != "" || $content[25] != "" || $content[26] != "") && $content[27] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[27] != "") {
                                                    echo "&#8226;  " . ucfirst($content[27]);
                                                }
                                                echo "<br>";
                                            }
                                            if ($content[28] != "" || $content[29] != "" || $content[30] != "") {
                                                ?>
                                                <strong>Other info: </strong> <br>
                                                <?php
                                                if ($content[28] != "") {
                                                    echo "&#8226;  " . ucfirst($content[28]);
                                                }
                                                if ($content[28] != "" && $content[29] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[29] != "") {
                                                    echo "&#8226;  " . ucfirst($content[29]);
                                                }
                                                if (($content[28] != "" || $content[29] != "") && $content[30] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[30] != "") {
                                                    echo "&#8226;  " . ucfirst($content[30]);
                                                }
                                            }
                                            ?>
                                        </p>
                                        <?php
                                    }
                                    if ($content[9] != "" || $content[8] != "" || $content[7] != "" || $content[16] != "") {
                                        ?>
                                        <?php
                                        if ($content[9] == "") {
                                            ?>
                                            <div class="wrapper style3 header_person to_hide_show">
                                                <?php
                                            } else {
                                                ?>
                                                <div class="wrapper style3 header_person">
                                                    <?php
                                                }
                                                ?>
                                                <div class="inner">
                                                    <div class="container header_person2">
                                                        <h3>Military</h3>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="person_info">
                                                <?php
                                                if ($content[9] != "") {
                                                    ?>
                                                    <strong>Stamboeknummer: </strong><?php echo $content[9]; ?>
                                                    <?php
                                                }
                                                ?>
                                                <span class="to_hide_show">
                                                    <?php
                                                    if ($content[9] != "" && $content[8] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[8] != "") {
                                                        ?>
                                                        <strong>Unit: </strong><?php echo ucfirst($content[8]); ?>
                                                        <?php
                                                    }
                                                    if (($content[9] != "" || $content[8] != "") && $content[7] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[7] != "") {
                                                        ?>
                                                        <strong>Rank: </strong><?php echo ucfirst($content[7]); ?>
                                                        <?php
                                                    }
                                                    if (($content[9] != "" || $content[8] != "" || $content[7] != "") && $content[16] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[16] != "") {
                                                        ?>
                                                        <strong>Destination report: </strong><?php echo ucfirst($content[16]); ?>
                                                    <?php } ?>
                                                </span>
                                            </p>
                                            <?php
                                        }
                                        if ($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "" || $content[6] != "" || $content[13] != "" || $content[14] != "" || $content[15] != "" || $content[12] != "") {
                                            ?>
                                            <div class="wrapper style3 header_person">
                                                <div class="inner">
                                                    <div class="container header_person2">
                                                        <h3>Biography</h3>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="person_info">
                                                <?php
                                                if ($content[42] != "") {
                                                    ?>
                                                    <strong>Nickname: </strong><?php echo ucfirst($content[42]); ?>
                                                    <?php
                                                }
                                                if ($content[42] != "" && $content[39] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[39] != "") {
                                                    ?>
                                                    <strong>Initials: </strong><?php echo ucfirst($content[39]); ?>
                                                    <?php
                                                }
                                                if (($content[42] != "" || $content[39] != "") && $content[2] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[2] != "") {
                                                    ?>
                                                    <strong>Surname: </strong><?php echo ucwords($content[2]); ?>
                                                    <?php
                                                }
                                                if (($content[42] != "" || $content[39] != "" || $content[2] != "") && $content[3] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[3] != "") {
                                                    ?>
                                                    <strong>Given names: </strong><?php echo ucwords($content[3]); ?>
                                                    <?php
                                                }
                                                ?>
                                                <span class="to_hide_show">
                                                    <?php
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "") && $content[4] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[4] != "") {
                                                        ?>
                                                        <strong>Infix: </strong><?php echo $content[4]; ?>
                                                        <?php
                                                    }
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "") && $content[38] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[38] != "") {
                                                        ?>
                                                        <strong>Gender: </strong><?php echo ucfirst($content[38]); ?>
                                                        <?php
                                                    }
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "") && $content[6] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[6] != "") {
                                                        ?>
                                                        <strong>Nationality: </strong><?php echo ucfirst($content[6]); ?>
                                                        <?php
                                                    }
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "" || $content[6] != "") && $content[13] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[13] != "") {
                                                        ?>
                                                        <strong>Father's name: </strong><?php echo ucwords($content[13]); ?>
                                                        <?php
                                                    }
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "" || $content[6] != "" || $content[13] != "") && $content[14] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[14] != "") {
                                                        ?>
                                                        <strong>Mother's name: </strong><?php echo ucwords($content[14]); ?>
                                                        <?php
                                                    }
                                                    if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "" || $content[6] != "" || $content[13] != "" || $content[14] != "") && $content[15] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[15] != "") {
                                                        ?>
                                                        <strong>Place of origin: </strong><?php echo ucfirst($content[15]); ?>
                                                        <?php
                                                    }
                                                    ?>
                                                </span>
                                                <?php
                                                if (($content[42] != "" || $content[39] != "" || $content[2] != "" || $content[3] != "" || $content[4] != "" || $content[38] != "" || $content[6] != "" || $content[13] != "" || $content[14] != "" || $content[15] != "") && $content[12] != "") {
                                                    echo "<br>";
                                                }
                                                if ($content[12] != "") {
                                                    ?>
                                                    <strong>Occupation: </strong><?php echo ucfirst($content[12]); ?>
                                                    <?php
                                                }
                                                ?>
                                            </p>
                                            <?php
                                        }
                                        ?>
                                        <span class="to_hide_show">
                                            <?php
                                            if ($content[34] != "" || $content[35] != "" || $content[36] != "" || $content[31] != "" || $content[17] != "" || $content[32] != "") {
                                                ?>
                                                <div class="wrapper style3 header_person">
                                                    <div class="inner">
                                                        <div class="container header_person2">
                                                            <h3>Internment cards</h3>
                                                        </div>
                                                    </div>
                                                </div>
                                                <p class="person_info">
                                                    <?php
                                                    if ($content[34] != "") {
                                                        ?>
                                                        <strong>Scan: </strong><?php
                                                        echo '<a href="' . $content[34] . '">' . $content[34] . "</a>";
                                                    }
                                                    if ($content[34] != "" && ($content[35] != "" || $content[36] != "")) {
                                                        echo "<br>";
                                                    }
                                                    if ($content[35] != "" || $content[36] != "") {
                                                        ?>
                                                        <strong>Reference: </strong> <br>
                                                        <?php
                                                        if ($content[35] != "") {
                                                            echo "&#8226;  " . strtoupper($content[35]);
                                                        }
                                                        if ($content[35] != "" && $content[36] != "") {
                                                            echo "<br>";
                                                        }
                                                        if ($content[36] != "") {
                                                            echo "&#8226;  " . $content[36];
                                                        }
                                                        ?>
                                                        <?php
                                                    }
                                                    if (($content[34] != "" || $content[35] != "" || $content[36] != "") && $content[31] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[31] != "") {
                                                        ?>
                                                        <strong>Serial number: </strong><?php echo ucfirst($content[31]); ?>
                                                        <?php
                                                    }
                                                    if (($content[34] != "" || $content[35] != "" || $content[36] != "" || $content[31] != "") && $content[17] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[17] != "") {
                                                        ?>
                                                        <strong>Remarks: </strong><?php echo ucfirst($content[17]); ?>
                                                        <?php
                                                    }
                                                    if (($content[34] != "" || $content[35] != "" || $content[36] != "" || $content[31] != "" || $content[17] != "") && $content[32] != "") {
                                                        echo "<br>";
                                                    }
                                                    if ($content[32] != "") {
                                                        ?>
                                                        <strong>Center top red letters: </strong><?php echo ucfirst($content[32]); ?>
                                                    <?php }
                                                    ?>
                                                </p>
                                                <?php
                                            }
                                            ?>
                                        </span>
                                        <span class="to_hide_show">
                                            <?php
                                            if ($content[44] != "") {
                                                ?>
                                                <div class="wrapper style3 header_person">
                                                    <div class="inner">
                                                        <div class="container header_person2">
                                                            <h3>Sources</h3>
                                                        </div>
                                                    </div>
                                                </div>
                                                <p class="person_info">
                                                    <?php
                                                    $source_list = explode(";", $content[44]);
                                                    for ($c = 0; $c < count($source_list); $c++) {
                                                        ?>
                                                        <?php
                                                        echo '&#8226;  <a href="' . $source_list[$c] . '">' . $source_list[$c] . "</a><br>";
                                                    }
                                                    ?>
                                                </p>
                                                <?php
                                            }
                                            ?>
                                        </span>
                                        <?php
                                        if ($content[43] != "") {
                                            ?>
                                            <div class="wrapper style3 header_person">
                                                <div class="inner">
                                                    <div class="container header_person2">
                                                        <h3>Images</h3>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="person_info" style="text-align:center;">
                                                <?php
                                                $image_list = explode(";", $content[43]);
                                                for ($c = 0; $c < count($image_list); $c++) {
                                                    ?>
                                                    <?php
                                                    echo '<a href="' . $image_list[$c] . '"><img src="' . $image_list[$c] . '" width="460"></a><br>';
                                                }
                                                ?>
                                            </p>
                                            <?php
                                        }
                                        if ($content[5] != "" || $content[11] != "" || $content[37] != "") {
                                            ?>
                                            <div class="wrapper style3 header_person">
                                                <div class="inner">
                                                    <div class="container header_person2">
                                                        <h3>Lifeline history</h3>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="person_info">
                                                <a href="timeline.php?id=<?php echo $content[0] ?>">
                                                    <?php
                                                    echo "Click here to see the lifeline history";
                                                    ?>
                                                </a>
                                            </p>
                                            <?php
                                        }
                                        ?>
                                        <div><button class="button_information" style="vertical-align:middle"><span class="information_text">Show more information</span></div>
                                </article>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="footer-wrapper">
                <footer id="footer" class="container">
                    <div class="row">
                        <div class="col-12">
                            <div id="copyright">
                                <ul class="menu">
                                    <li>&copy; Vrije Universiteit Amsterdam. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
        </div>

        <script src="assets/js/jquery.min.js"></script>
        <script src="assets/js/jquery.dropotron.min.js"></script>
        <script src="assets/js/browser.min.js"></script>
        <script src="assets/js/breakpoints.min.js"></script>
        <script src="assets/js/util.js"></script>
        <script src="assets/js/main.js"></script>

    </body>
</html>