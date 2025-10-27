

contacts = { "Nazar":{"instagram":"lakusta.nazar",
"telegram":"nazarko1703", "phone":"3809545454"},

"Vlad":{"instagram":"vladoisi",
"telegram":"vladsadas", "phone":"3805345435434"},


"Serhiy":{"instagram":"serik",
"telegram":"seriraka", "phone":"380965654"}

}


info = contacts[input("Чиї контакти  хочеш дізнатися?: ")][input("Яку соц мережу хочете дізнатись?")]
print(info)










translator = {"hello":"привіт", "bye" : "пака", "step":"крок"}
word = input("Яке слово хоче перекласти? з англ на укр: ")
print(translator[word])