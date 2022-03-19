#!/bin/csh -f
set nonomatch

if ($#argv == 0) then
  set par = ""
else
  set par = $argv[1]
endif

if ($par == "portal" || $par == "all") then
  rm -f Portal/*.dxf
  python3.8 ./Portal-Plate.py
endif

if ($par == "frame" || $par == "all") then
  rm -f Frame/*.dxf
  python3.8 ./Frame-Plate.py
endif

if ($par == "z-axis" || $par == "all") then
  rm -f Z-Axis/*.dxf
  python3.8 ./Z-Axis-Plate.py
endif

if ($par == "extrusion" || $par == "all") then
  rm -f XYZ-Extrusion.txt
  python3.8 ./XYZ-Extrusion.py
endif

