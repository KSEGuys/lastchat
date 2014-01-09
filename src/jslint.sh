for file in $(find . -name "*.js" -not -name "jquery.*.js")
do
    jslint -process $file
done
