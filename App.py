from MidWare.ReadLanguageJson import ReadLanguageJson
from MidWare.SelectLanguage import SelectLanguage
from MidWare.UserPromt import UserPromt

language = ReadLanguageJson().main()
SelectLanguage.language = language

if language not in ['English', 'Türkçe']:
    
    SelectLanguage().main()  
    UserPromt().main()

else:
    UserPromt().main()