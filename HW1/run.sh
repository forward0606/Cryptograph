cipher=("AESCBC" "AESCTR" "ChaCha20")

for i in ${cipher[@]}
do
    cd $i
    echo "running $i"
    rm *.txt
    time python3 encrypt.py
    python3 decrypt.py
    echo "diff retrive.txt ../plaintext.txt"
    diff retrive.txt ../plaintext.txt
    cd ../
done
    
