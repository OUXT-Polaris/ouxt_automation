xhost +local:

cd $OUXT_AUTOMATION && docker compose start && docker compose exec robotx_ws gosu ros bash
