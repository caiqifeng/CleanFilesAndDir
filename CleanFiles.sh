echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clena Start...."
find /home/mechawar/Rundata/ReplayFiles/ -type f -mmin +720 -delete
echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clean ReplayFiles...... Done"
find /home/mechawar/Rundata/TLog/ -type f -mmin +720 -delete
echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clean TLog...... Done"
find /home/mechawar/Runtime/Log/ -type f -mmin +720 -delete
echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clean Log...... Done"
find /home/mechawar/ -type f -name 'core.*' -mtime -7200 -exec rm {} \;
echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clean core.* ...... Done"
echo "[$(date +"%Y-%m-%d %H:%M:%S.%N")]Clean End"

