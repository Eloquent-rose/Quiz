import time

class Quizzieee:

    def __init__(self):
        self.total_score = 0
        self.NOP = 0
        self.percentage = 0.0
        self.NOQ = 0
        self.name = ""

    def Welcome( self ):
        print( "-----------------------------------------------------------------------------------------------" )
        self.name = input( "Hello! We will be very delightful to know your name: " )
        print( f"--------------------------------- Welcome to your quiz {self.name}! -----------------------------------" )
        time.sleep(2)
        print( "------------------------------------- Glad you are here!! -----------------------------------" )
        time.sleep(2)
        print( "----------------------------------- Your quiz will start in  ------------------------------" )
        time.sleep(2)
        print( "3........" )
        time.sleep(1)
        print( "2......." )
        time.sleep(1)
        print("1......!!")
        time.sleep(1)

        print( "-----------------------------------------------------------------------------------------------" )
    
    def check_number_in_string( self, string_input ):
        for i in string_input:
            if i.isnumeric():
                return int(i)
        
        return self.total_score

    def extraction( self ):
        question_dictionary = {}
        keys = ["Questions", "NOA", "Options", "Answers"]

        doc = open( "E:/Programs/Quiz/questions.txt", 'r' )
        doc_file = doc.read();
        doc_list = doc_file.split( "---------------------------------------------------------" )
        
        for i in range(len(doc_list)):
            value = doc_list[i].split( "\n\n" )

            if len( keys ) == len( value ):
                for j in range( len(value) ):
                    question_dictionary[keys[j]] = value[j]

            else:
                question_dictionary[keys[0]] = value[0]
                question_dictionary[keys[1]] = 1
                question_dictionary[keys[2]] = value[1]
                question_dictionary[keys[3]] = value[2]
                

            print( question_dictionary["Questions"] )
            if question_dictionary["NOA"] != 1:
                print( question_dictionary["NOA"] )
            print( question_dictionary["Options"] )

            self.NOQ = self.NOQ + 1

            if question_dictionary["NOA"] != 1:
                number = self.check_number_in_string( question_dictionary["NOA"] )
                question_dictionary[keys[1]] = number
            
            final_ans = ""
            self.NOP = self.NOP + question_dictionary[keys[1]]

            for i in range( question_dictionary[keys[1]] ):
                ans = input( f"Enter option {i+1}: " )
                final_ans = final_ans + ans.upper()

            actual_ans = question_dictionary["Answers"].replace( "ANS => ", "" ).replace( ", ", "" ).replace( "\n", "" )

            for i in range( len( final_ans ) ):
                if final_ans[i] == actual_ans[i]:
                    self.total_score = self.total_score + 1
            

            if final_ans == actual_ans:
                print( "Yayyy! Got it right." )
            else:
                print( f"Close enough, {question_dictionary['Answers']}" )

    def results_summary( self ):

        self.percentage = (self.total_score / self.NOP) * 100
        print( "-----------------------------------------------------------------------------------------------" )
        print( f"Hello {self.name}" )
        time.sleep(2)
        print( "You successfully completed the quiz!" )
        time.sleep(2)
        print( "Now let us see the results.... fingers crossed!" )
        time.sleep(2)
        print( "In 3........" )
        time.sleep(1)
        print( "2........" )
        time.sleep(1)
        print( "1........" )
        time.sleep(1)
        print( "-----------------------------------------------------------------------------------------------" )

        print( f"Number of Questions which were given to you: {self.NOQ}" )
        print( f"Number of Questions you attempted: {self.NOQ}" )
        print( f"Total Score for evaluation: {self.NOP}" )
        print( f"Points you have been awarded for each correct answer: {self.total_score}" )

        print( f"Your percentage: {self.percentage}" )
        if self.percentage > 80.0:
            print( "You have done an amazing work! Keep it up..!" )
        
        elif self.percentage > 60.0 and self.percentage < 79.9:
            print( "Good job champ...!" )

        elif self.percentage > 40.0 and self.percentage < 59.9:
            print( "Keep working..you can do it!" )

        else:
            print( "Its okay! Don't give up...!" )
        
        print( "-----------------------------------------------------------------------------------------------" )
            

if __name__ == '__main__':

    myObject = Quizzieee()
    myObject.Welcome()
    myObject.extraction()
    myObject.results_summary()

