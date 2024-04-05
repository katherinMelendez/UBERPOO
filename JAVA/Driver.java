class Driver extends Account {

    public Driver(String name, String document, String email, String password){
        super(name, document, email, password);
    }
void printDataDriver(){
    System.out.prinln("Document 
    drive:" + document +  " Name
    driver: " + name + " e-mail: "
    +  email + "Password: "+ password);
}
}