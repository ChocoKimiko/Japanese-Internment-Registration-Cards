<!DOCTYPE html>
<?php
date_default_timezone_set('UTC');
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
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                background-color: #24262B;
                font-family: Helvetica, sans-serif;
            }

            /* The actual timeline (the vertical ruler) */
            .timeline {
                position: relative;
                max-width: 1200px;
                margin: 0 auto;
            }

            /* The actual timeline (the vertical ruler) */
            .timeline::after {
                content: '';
                position: absolute;
                width: 6px;
                background-color: white;
                top: 0;
                bottom: 0;
                left: 50%;
                margin-left: -3px;
            }

            /* Container around content */
            .container {
                padding: 10px 40px;
                position: relative;
                background-color: inherit;
                width: 50%;
            }

            /* The circles on the timeline */
            .container::after {
                content: '';
                position: absolute;
                width: 25px;
                height: 25px;
                right: -17px;
                background-color: #B2B2B2;
                border: 4px solid white;
                top: 15px;
                border-radius: 50%;
                z-index: 1;
            }

            /* Place the container to the left */
            .left {
                left: 0;
            }

            /* Place the container to the right */
            .right {
                left: 50%;
            }

            /* Add arrows to the left container (pointing right) */
            .left::before {
                content: " ";
                height: 0;
                position: absolute;
                top: 22px;
                width: 0;
                z-index: 1;
                right: 30px;
                border: medium solid white;
                border-width: 10px 0 10px 10px;
                border-color: transparent transparent transparent white;
            }

            /* Add arrows to the right container (pointing left) */
            .right::before {
                content: " ";
                height: 0;
                position: absolute;
                top: 22px;
                width: 0;
                z-index: 1;
                left: 30px;
                border: medium solid white;
                border-width: 10px 10px 10px 0;
                border-color: transparent white transparent transparent;
            }

            /* Fix the circle for containers on the right side */
            .right::after {
                left: -16px;
            }

            /* The actual content */
            .content {
                padding: 20px 30px;
                background-color: white;
                position: relative;
                border-radius: 6px;
            }

            /* Media queries - Responsive timeline on screens less than 600px wide */
            @media screen and (max-width: 600px) {
                /* Place the timelime to the left */
                .timeline::after {
                    left: 31px;
                }

                /* Full-width containers */
                .container {
                    width: 100%;
                    padding-left: 70px;
                    padding-right: 25px;
                }

                /* Make sure that all arrows are pointing leftwards */
                .container::before {
                    left: 60px;
                    border: medium solid white;
                    border-width: 10px 10px 10px 0;
                    border-color: transparent white transparent transparent;
                }

                /* Make sure all circles are at the same spot */
                .left::after, .right::after {
                    left: 15px;
                }

                /* Make all right containers behave like the left ones */
                .right {
                    left: 0%;
                }
            }
        </style>
    </head>
    <body>
        <header class="major" style="text-align:center; color:#FFFFFF; border-bottom: solid 1px #dbdbdb; margin: 0 0 1em 0;">
            <h2><?php echo strtoupper($content[1]) . "'S LIFELINE HISTORY"; ?></h2>
        </header>
        <div class="timeline">
            <?php
            if ($content[5] != "") {
                ?>
                <div class="container left">
                    <div class="content">
                        <h2>
                            <?php
                            echo substr($content[5], 0, 4);
                            ?>
                        </h2>
                        <p>
                            <?php
                            $birth_date = date_create($content[5]);
                            if ($content[5] != "" && $content[40] != "") {
                                echo "Mr. " . ucwords($content[1]) . " was born on the " . date_format($birth_date, "jS \of F Y") . " in " . ucfirst($content[40]) . ".";
                            } else if ($content[5] != "" && $content[40] == "") {
                                echo "Mr. " . ucwords($content[1]) . " was born on the " . date_format($birth_date, "jS \of F Y") . ".";
                            }
                            ?>
                        </p>
                    </div>
                </div>
                <?php
            }
            if ($content[11] != "") {
                ?>
                <div class="container right">
                    <div class="content">
                        <h2>
                            <?php
                            echo substr($content[11], 0, 4);
                            ?>
                        </h2>
                        <p>
                            <?php
                            $capture_date = date_create($content[11]);
                            if ($content[11] != "" && $content[10] != "") {
                                echo "Mr. " . ucwords($content[1]) . " was captured on the " . date_format($capture_date, "jS \of F Y") . " in " . ucfirst($content[10]) . ".";
                            } else if ($content[11] != "" && $content[10] == "") {
                                echo "Mr. " . ucwords($content[1]) . " was captured on the " . date_format($capture_date, "jS \of F Y") . ".";
                            }
                            if ($content[18] != "" || $content[19] != "" || $content[20] != "" || $content[21] != "" || $content[22] != "") {
                                ?>
                                <br><br><strong>Camp and transfer date: </strong> <br>
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
                            }
                            echo "<br>";
                            if ($content[23] != "" || $content[24] != "" || $content[25] != "" || $content[26] != "" || $content[27] != "") {
                                ?>
                                <br><strong>Camp branch name and registration number: </strong> <br>
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
                            ?>
                        </p>
                    </div>
                </div>
                <?php
            }
            if ($content[37] != "") {
                ?>
                <div class="container left">
                    <div class="content">
                        <h2>
                            <?php
                            echo substr($content[37], 0, 4);
                            ?>
                        </h2>
                        <p>
                            <?php
                            $death_date = date_create($content[37]);
                            if ($content[37] != "" && $content[41] != "") {
                                echo "Mr. " . ucwords($content[1]) . " died on the " . date_format($death_date, "jS \of F Y") . " in " . ucfirst($content[41]) . ".";
                            } else if ($content[37] != "" && $content[41] == "") {
                                echo "Mr. " . ucwords($content[1]) . " died on the " . date_format($death_date, "jS \of F Y") . ".";
                            }
                            ?>
                        </p>
                    </div>
                </div>
                <?php
            }
            ?>
        </div>
    </body>
</html>
