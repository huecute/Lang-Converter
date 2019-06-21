class CPlus:
    def CPlusToJava(word, self):
        if "#include" in self:
            return "BlankSpace"
        if "using namespace" in self:
            return "public Class Temp Name{"
        if "int main()" in self:
            return self.replace("int main()", "public static void main(String[] args)")
        if "cout << " in self:
            if "endl" in self:
                self = self.replace('endl', '"\\n"')
            self = self.replace("cout << ", "System.out.print(")
            self = self.replace("<<", '+' )
            self = self.replace(";", ");")
            return self
        if "return 0" in self:
            return "\t}"
        else:
            return self

    def CPlusToPython(word, self):
        if "#include" in self:
            return "BlankSpace"
        if "using namespace" in self:
            return "BlankSpace"
        if "int main()" in self:
            return "BlankSpace"
        if '}' in self:
            return "BlankSpace"
        if "cout << " in self:
            if "endl" in self:
                self = self.replace('endl', '"\\n"')
            self = self.replace("cout << ", "print(")
            self = self.replace("<<", '+' )
            self = self.replace(";", ")")
            return self
        if "return 0" in self:
            return "BlankSpace"
        if (';' in self):
             self = self.replace(';', ' ')
             return self
        else:
            return self
     
class Java:
    def JavaToCPlus(word, self):
        if "#public Class" in self:
            return "#include <iostream> \nusing namespace std;"
        if "public static void" in self:
            return self.replace("public static void main(String[] args)", "int main()")
        if "System.out.print" in self:
            if "println" in self:
                self = self.replace('System.out.println(', 'cout << ')
                self = self.replace(');', ' << endl;')
                self = self.replace(' + ', " << ")
            else:
                self = self.replace("System.out.print( ", "cout << ")
                self = self.replace("+", '<<' )
                self = self.replace(");", ";")
            return self
        if "return 0" in self:
            return "\t}"
        else:
            return self

    def JavaToPython(word, self):
        if "public Class" in self:
            return "BlankSpace"
        if "public static void main" in self:
            return "BlankSpace"
        if '}' in self:
            return "BlankSpace"
        if "System.out.print" in self:
            if "println(" in self:
                self = self.replace('System.out.println(', 'print(')
                self = self.replace(');', '\\n)')
            else:
                self = self.replace("System.out.print(", "print(")
                self = self.replace(";", ")")
            return self
        if (';' in self):
             self = self.replace(';', ' ')
             return self
        else:
            return self


print("What language are you converting?")
lang1 = input("A. Java\nB. C++\n")
print("What language are you converting to?")
lang2 = input("A. Java\nB. C++\nC. Python\n")
file1 = input("What is the name of the file you are getting your code?")
file2 = input("What is the name of the file you are writing to?")
with open(file2, 'w') as file:
    with open(file1, 'rU') as f:
        if(lang1 == "B" or lang1 == "b"):
            CP = CPlus()
            if(lang2 == 'c' or lang2 == 'C'):
                for l in f:
                    line = CP.CPlusToPython(l)
                    if 'BlankSpace' not in line:
                        file.write(line + '\n')
            elif(lang1 == "A" or lang2 == "a"):
                for l in f:
                    line = CP.CPlusToJava(l)
                    if 'BlankSpace' not in line:
                        file.write(line + "\n")
            elif(lang1 == "B" or lang2 == "b"):
                for l in f:
                    file.write(l)
        if(lang1 == "A" or lang1 == "a"):
            J = Java()
            if(lang2 == 'c' or lang2 == 'C'):
                for l in f:
                    line = J.JavaToPython(l)
                    if 'BlankSpace' not in line:
                        file.write(line + '\n')
            elif(lang1 == "B" or lang2 == "b"):
                for l in f:
                    line = J.JavaToCPlus(l)
                    if 'BlankSpace' not in line:
                        file.write(line + "\n")
            elif(lang1 == "A" or lang2 == "a"):
                for l in f:
                    file.write(l)  
