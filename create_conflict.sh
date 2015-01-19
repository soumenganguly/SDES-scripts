while read line
do
    name=$line
    mkdir /tmp/$name

    if [ "$?" -ne "0" ]; then
        echo "Submission failed"
        exit 1
    fi

    echo -e "Name: Student T\nCourse: MBBS\nDepartment: Medical Sciences\nRoll number: JB007\nYear: Infinite\nResearch/study interests:\nBrain surgery, heart disease, foot in mouth disease." >> ./$name/README.md

echo "Done Creating Files"
done < $1
