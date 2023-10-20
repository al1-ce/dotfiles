if [ $# -eq 0 ]; then
    echo "Missing script name"
    exit 0
fi

mkdir -p ~/.local/scripts

touch ~/.local/scripts/$1
echo "#!/usr/bin/env rund" >> ~/.local/scripts/$1
echo "# This is a dummy script to be able" >> ~/.local/scripts/$1
echo "# to run code without .d extension" >> ~/.local/scripts/$1
echo "# real script is at ~/.local/scripts/$1" >> ~/.local/scripts/$1
chmod +x ~/.local/scripts/$1

echo "Dummy created at ~/.local/scripts/$1"

touch ~/.local/scripts/$1.d
echo "import std.stdio: writeln;" >> ~/.local/scripts/$1.d
echo "" >> ~/.local/scripts/$1.d
echo "void main() {" >> ~/.local/scripts/$1.d
echo '    writeln("Edit script first.");' >> ~/.local/scripts/$1.d
echo '}' >> ~/.local/scripts/$1.d

echo "Script created at ~/.local/scripts/$1.d"