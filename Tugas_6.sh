echo "Input semester :"
read semester

# deklarasi array nilai IPS
declare -a nilaiIPS

i=0
let banyak=$semester-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  printf "nilai Semester %.1i = " $angka;
  read nilaisemester;
  nilaiIPS[$i]=$nilaisemester;
  let jumlah=jumlah+$nilaisemester;
  let i=$i+1;
done

let IPK=$jumlah/$semester


# pengambilan nilai array
echo "nilai IPS Mahasiswa tiap semester : ${nilaiIPS[@]}"
echo "jumlah nilai IPS / banyaknya nilai IPS :" $jumlah "/" $semester
echo "IPK Mahasiswa :" $IPK
