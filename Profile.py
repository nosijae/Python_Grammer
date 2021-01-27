# def profile(name, age=17, main_lang="Python"):
#     print("Name: {0}\tAge: {1}\tMain language: {2}" \
#           .format(name, age, main_lang))
#
#
# profile("Audu")
# profile("Suna")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name: {0}\tage: {1}\t".format(name, age), end=" ")
#     # end를 빈칸으로 하면 문장 출력후 이어서 밑에 있는 문장을 바로 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("name: {0}\tage: {1}\t".format(name, age), end=" ")
    # end를 빈칸으로 하면 문장 출력후 이어서 밑에 있는 문장을 바로 출력
    for lang in language:
        print(lang, end=" ")
    print()


profile("noh", 20, "python", "java", "C", "C++", "C#", "javaScript")
profile("kim", 25, "Kotlin", "Swift", "", "", "")


