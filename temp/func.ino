void folder() {
  int xx, yy, zz, pullback[16], state = 0, backorfront = 7;

  int folderaddr[16], LED_Old[16], oldpullback[16], ranx = random(16), rany = random(16), ranz = random(16), ranselect;
  int bot = 0, top = 1, right = 0, left = 0, back = 0, front = 0, side = 0, side_select;

  folderaddr[0] = -7;
  folderaddr[1] = -6;
  folderaddr[2] = -5;
  folderaddr[3] = -4;
  folderaddr[4] = -3;
  folderaddr[5] = -2;
  folderaddr[6] = -1;
  folderaddr[7] = 0;

  for (xx = 0; xx < 8; xx++) {
    oldpullback[xx] = 0;
    pullback[xx] = 0;
  }



  start = millis();
  while (millis() - start < 10000) {
    if (top == 1) {
      if (side == 0) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(7 - LED_Old[yy], yy - oldpullback[yy], xx , 0, 0, 0);
            LED(7 - folderaddr[yy], yy - pullback[yy], xx , ranx, rany, ranz);
          }
        }
      }
      if (side == 2) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(7 - LED_Old[yy], xx, yy - oldpullback[yy], 0, 0, 0);
            LED(7 - folderaddr[yy], xx, yy - pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 3) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(7 - LED_Old[7 - yy], xx, yy + oldpullback[yy], 0, 0, 0);
            LED(7 - folderaddr[7 - yy], xx, yy + pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 1) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(7 - LED_Old[7 - yy], yy + oldpullback[yy], xx , 0, 0, 0);
            LED(7 - folderaddr[7 - yy], yy + pullback[yy], xx , ranx, rany, ranz);
          }
        }
      }
    }

    if (right == 1) {
      if (side == 4) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy + oldpullback[7 - yy], 7 - LED_Old[7 - yy], xx , 0, 0, 0);
            LED( yy + pullback[7 - yy], 7 - folderaddr[7 - yy], xx , ranx, rany, ranz);
          }
        }
      }
      if (side == 3) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, 7 - LED_Old[7 - yy], yy + oldpullback[yy], 0, 0, 0);
            LED(xx, 7 - folderaddr[7 - yy], yy + pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 2) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, 7 - LED_Old[yy], yy - oldpullback[yy], 0, 0, 0);
            LED(xx, 7 - folderaddr[yy], yy - pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 5) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy - oldpullback[yy], 7 - LED_Old[yy], xx , 0, 0, 0);
            LED( yy - pullback[yy], 7 - folderaddr[yy], xx , ranx, rany, ranz);
          }
        }
      }
    }

    if (left == 1) {
      if (side == 4) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy + oldpullback[yy], LED_Old[7 - yy], xx , 0, 0, 0);
            LED( yy + pullback[yy], folderaddr[7 - yy], xx , ranx, rany, ranz);
          }
        }
      }
      if (side == 3) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, LED_Old[7 - yy], yy + oldpullback[yy], 0, 0, 0);
            LED(xx, folderaddr[7 - yy], yy + pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 2) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, LED_Old[yy], yy - oldpullback[yy], 0, 0, 0);
            LED(xx, folderaddr[yy], yy - pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 5) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy - oldpullback[yy], LED_Old[yy], xx , 0, 0, 0);
            LED( yy - pullback[yy], folderaddr[yy], xx , ranx, rany, ranz);
          }
        }
      }
    }


    if (back == 1) {
      if (side == 1) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, yy + oldpullback[yy], LED_Old[7 - yy], 0, 0, 0);
            LED(xx, yy + pullback[yy], folderaddr[7 - yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 4) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy + oldpullback[yy], xx, LED_Old[7 - yy] , 0, 0, 0);
            LED( yy + pullback[yy], xx, folderaddr[7 - yy] , ranx, rany, ranz);
          }
        }
      }
      if (side == 5) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy - oldpullback[yy], xx, LED_Old[yy] , 0, 0, 0);
            LED( yy - pullback[yy], xx, folderaddr[yy] , ranx, rany, ranz);
          }
        }
      }
      if (side == 0) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, yy - oldpullback[yy], LED_Old[yy], 0, 0, 0);
            LED(xx, yy - pullback[yy], folderaddr[yy], ranx, rany, ranz);
          }
        }
      }
    }
    if (bot == 1) {
      if (side == 1) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(LED_Old[7 - yy], yy + oldpullback[yy], xx , 0, 0, 0);
            LED(folderaddr[7 - yy], yy + pullback[yy], xx , ranx, rany, ranz);
          }
        }
      }
      if (side == 3) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(LED_Old[7 - yy], xx, yy + oldpullback[yy], 0, 0, 0);
            LED(folderaddr[7 - yy], xx, yy + pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 2) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(LED_Old[yy], xx, yy - oldpullback[yy], 0, 0, 0);
            LED(folderaddr[yy], xx, yy - pullback[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 0) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(LED_Old[yy], yy - oldpullback[yy], xx , 0, 0, 0);
            LED(folderaddr[yy], yy - pullback[yy], xx , ranx, rany, ranz);
          }
        }
      }
    }

    if (front == 1) {
      if (side == 0) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, yy - oldpullback[yy], 7 - LED_Old[yy], 0, 0, 0);
            LED(xx, yy - pullback[yy], 7 - folderaddr[yy], ranx, rany, ranz);
          }
        }
      }
      if (side == 5) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy - oldpullback[yy], xx, 7 - LED_Old[yy] , 0, 0, 0);
            LED( yy - pullback[yy], xx, 7 - folderaddr[yy] , ranx, rany, ranz);
          }
        }
      }
      if (side == 4) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(yy + oldpullback[yy], xx, 7 - LED_Old[7 - yy] , 0, 0, 0);
            LED( yy + pullback[yy], xx, 7 - folderaddr[7 - yy] , ranx, rany, ranz);
          }
        }
      }
      if (side == 1) {

        for (yy = 0; yy < 8; yy++) {
          for (xx = 0; xx < 8; xx++) {
            LED(xx, yy + oldpullback[yy], 7 - LED_Old[7 - yy], 0, 0, 0);
            LED(xx, yy + pullback[yy], 7 - folderaddr[7 - yy], ranx, rany, ranz);
          }
        }
      }
    }




    delay(5);
    for (xx = 0; xx < 8; xx++) {
      LED_Old[xx] = folderaddr[xx];
      oldpullback[xx] = pullback[xx];
    }





    if (folderaddr[7] == 7) {

      for (zz = 0; zz < 8; zz++)
        pullback[zz] = pullback[zz] + 1;

      if (pullback[7] == 8) {
        delay(10);




        ranselect = random(3);
        if (ranselect == 0) {
          ranx = 0;
          rany = random(1, 16);
          ranz = random(1, 16);
        }
        if (ranselect == 1) {
          ranx = random(1, 16);
          rany = 0;
          ranz = random(1, 16);
        }
        if (ranselect == 2) {
          ranx = random(1, 16);
          rany = random(1, 16);
          ranz = 0;
        }

        side_select = random(3);

        if (top == 1) {
          top = 0;
          if (side == 0) {
            left = 1;
            if (side_select == 0) side = 2;
            if (side_select == 1) side = 3;

            if (side_select == 2) side = 5;
          } else if (side == 1) {
            right = 1;
            if (side_select == 0) side = 5;
            if (side_select == 1) side = 2;
            if (side_select == 2) side = 3;

          } else if (side == 2) {
            back = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 1;
            if (side_select == 2) side = 5;

          } else if (side == 3) {
            front = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 1;
            if (side_select == 2) side = 5;

          }
        } else if (bot == 1) {
          bot = 0;
          if (side == 0) {
            left = 1;
            if (side_select == 0) side = 2;
            if (side_select == 1) side = 3;
            if (side_select == 2) side = 4;

          } else if (side == 1) {
            right = 1;

            if (side_select == 0) side = 2;
            if (side_select == 1) side = 3;
            if (side_select == 2) side = 4;
          } else if (side == 2) {
            back = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 1;

            if (side_select == 2) side = 4;
          } else if (side == 3) {
            front = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 1;

            if (side_select == 2) side = 4;
          }
        } else if (right == 1) {
          right = 0;
          if (side == 4) {
            top = 1;
            if (side_select == 0) side = 2;
            if (side_select == 1) side = 3;
            if (side_select == 2) side = 0;

          } else if (side == 5) {
            bot = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 2;
            if (side_select == 2) side = 3;

          }
          else if (side == 2) {
            back = 1;
            if (side_select == 0) side = 0;

            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          } else if (side == 3) {
            front = 1;
            if (side_select == 0) side = 0;

            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          }
        } else if (left == 1) {
          left = 0;
          if (side == 4) {
            top = 1;

            if (side_select == 0) side = 3;
            if (side_select == 1) side = 2;
            if (side_select == 2) side = 1;
          } else if (side == 5) {
            bot = 1;

            if (side_select == 0) side = 2;
            if (side_select == 1) side = 3;
            if (side_select == 2) side = 1;
          } else if (side == 2) {
            back = 1;

            if (side_select == 0) side = 1;
            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          } else if (side == 3) {
            front = 1;

            if (side_select == 0) side = 1;
            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          }
        } else if (front == 1) {
          front = 0;
          if (side == 4) {
            top = 1;
            if (side_select == 0) side = 2;

            if (side_select == 1) side = 0;
            if (side_select == 2) side = 1;
          } else if (side == 5) {
            bot = 1;
            if (side_select == 0) side = 0;
            if (side_select == 1) side = 2;

            if (side_select == 2) side = 1;
          } else if (side == 0) {
            left = 1;
            if (side_select == 0) side = 2;

            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          } else if (side == 1) {
            right = 1;
            if (side_select == 0) side = 2;

            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          }
        } else if (back == 1) {
          back = 0;
          if (side == 4) {
            top = 1;

            if (side_select == 0) side = 3;
            if (side_select == 1) side = 0;
            if (side_select == 2) side = 1;
          } else if (side == 5) {
            bot = 1;
            if (side_select == 0) side = 0;

            if (side_select == 1) side = 3;
            if (side_select == 2) side = 1;
          } else if (side == 0) {
            left = 1;

            if (side_select == 0) side = 3;
            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          } else if (side == 1) {
            right = 1;

            if (side_select == 0) side = 3;
            if (side_select == 1) side = 5;
            if (side_select == 2) side = 4;
          }
        }





        for (xx = 0; xx < 8; xx++) {
          oldpullback[xx] = 0;
          pullback[xx] = 0;
        }

        folderaddr[0] = -8;
        folderaddr[1] = -7;
        folderaddr[2] = -6;
        folderaddr[3] = -5;
        folderaddr[4] = -4;
        folderaddr[5] = -3;
        folderaddr[6] = -2;
        folderaddr[7] = -1;

      }
    }

    if (folderaddr[7] != 7)
      for (zz = 0; zz < 8; zz++)
        folderaddr[zz] = folderaddr[zz] + 1;

  }





}