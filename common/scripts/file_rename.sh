n=1
for file in $(ls -1v *.{jpg,jpeg,png,JPG,JPEG,PNG} 2>/dev/null); do
  [ -e "$file" ] || continue  # Skip non-existing matches
  ext="${file##*.}"
  new_name=$(printf "rose_%03d.%s" "$n" "$ext")
  mv -- "$file" "$new_name"
  ((n++))
done