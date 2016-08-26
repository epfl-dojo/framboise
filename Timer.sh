#!/bin/bash

echo "Welcome we're transforming your pi into a Timer..."

echo "We're checking if you have all the requiered programs..."
requieredPrograms=(git python3 pygame alsa bite)
i=0; n=0;
for p in "${requieredPrograms[@]}"; do
    if hash "$p" &>/dev/null
    then
        echo "$p is installed"
        let c++
    else
        echo "$p is not installed"
        let n++
    fi
done
printf "%d of %d programs were installed.\n"  "$i" "${#requieredPrograms[@]}"
printf "%d of %d programs were missing\n" "$n" "${#requieredPrograms[@]}"


#git clone https://github.com/epfl-dojo/framboise.git
