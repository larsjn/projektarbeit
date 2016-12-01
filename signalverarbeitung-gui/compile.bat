@echo off
del gui_jupyther_main.py
del ..\jupyter\gui_jupyter_main.py
echo del done
pause
start pyuic4.bat -x mainwindow.ui -o gui_jupyter_main.py
echo compile done
pause
copy "gui_jupyter_main.py" "..\jupyter\gui_jupyter_main.py"
echo copy done
exit