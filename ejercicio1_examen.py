
from datetime import datetime
from email import Email

class UserAccount:
    """
    alias (str): Se utiliza un str para representar el alias del usuario,
     ya que generalmente los alias son cadenas de texto.

    email (Email): Se asume que existe una clase Email que representa la dirección
    de correo electrónico del usuario. Utilizamos esta clase para asegurar que el email
    cumple con ciertas validaciones y para encapsular la lógica relacionada con los emails.

    tweets (List[Tweet]): Se utiliza una lista (List) para almacenar los tweets publicados
    por el usuario. Cada tweet se representa con un objeto de la clase Tweet.

    followers (List[UserAccount]): Se utiliza una lista (List) para almacenar los seguidores
    del usuario. Cada seguidor se representa con un objeto de la clase UserAccount.

    timeline (List[Tweet]): Se utiliza una lista (List) para almacenar los tweets recibidos
    en el timeline del usuario. Cada tweet se representa con un objeto de la clase Tweet.

    """

    def __init__(self, alias: str, email: Email):
        """
        Constructor de la clase UserAccount
        """
        self.alias = alias
        self.email = email
        self.tweets = []
        self.followers = []
        self.timeline = []

    def follow(self, user2: 'UserAccount'):
        """
        Permite que el usuario actual siga a otro usuario

        Parámetros:
        - user2 (UserAccount): El usuario al que se desea seguir

        """
        user2.add_follower(self)

    def add_follower(self, follower: 'UserAccount'):
        """
        Agrega un seguidor a la lista de followers del usuario

        Parámetros:
        - follower (UserAccount): El usuario seguidor a agregar

        """
        self.followers.append(follower)

    def tweet(self, tweet1: Tweet):
        """
        Permite que el usuario actual publique un tweet

        Parámetros:
        - tweet1 (Tweet): El tweet a publicar

        """
        self.tweets.append(tweet1)
        self.notify_followers(tweet1)

    def notify_followers(self, tweet: Tweet):
        """
        Notifica a los seguidores del usuario

        Parámetros:
        - tweet (Tweet): El tweet a notificar

        """
        for follower in self.followers:
            follower.receive_tweet(tweet)

    def receive_tweet(self, tweet: Tweet):
        """
        Recibe un tweet y lo añade al timeline del usuario

        Parámetros:
        - tweet (Tweet): El tweet recibido

        """
        self.timeline.append(tweet)


class Tweet:
    """
    Representa un tweet

    Atributos:
    - message (str): El mensaje
    - time (datetime): La fecha y hora de creación
    - sender (UserAccount): El usuario remitente

    """

    MAX_MESSAGE_LENGTH = 140

    def __init__(self, message: str, sender: UserAccount):
        """
        Constructor de la clase Twee

        Parámetros:
        - message (str):
        - sender (UserAccount):

        """
        if len(message) > self.MAX_MESSAGE_LENGTH:
            raise ValueError("El mensaje excede la longitud máxima permitida.")
        self.message = message
        self.time = datetime.now()
        self.sender = sender

    def __str__(self):
        return f"Tweet from {self.sender.alias} at {self.time}: {self.message}"


class DirectMessage(Tweet):
    """
    Representa un mensaje directo

    Atributos:
    - message (str): El mensaje en si
    - time (datetime): La fecha y hora de creación
    - sender (UserAccount): El usuario remitente
    - receiver (UserAccount): El usuario destinatario

    """

    def __init__(self, message: str, sender: UserAccount, receiver: UserAccount):
        """
        Constructor de la clase DirectMessage

        Parámetros:
        - message (str):
        - sender (UserAccount):
        - receiver (UserAccount):

        """
        super().__init__(message, sender)
        self.receiver = receiver

    def __str__(self):
        return f"Direct Message from {self.sender.alias} to {self.receiver.alias} at {self.time}: {self.message}"


class Retweet(Tweet):
    """
    Representa un retweet

    Atributos:
    - message (str): El mensaje
    - time (datetime): La fecha y hora de creación
    - sender (UserAccount): El usuario que publica
    - tweet (Tweet): El tweet que se reenvía

    """

    def __init__(self, message: str, sender: UserAccount, tweet: Tweet):
        """
        Constructor de la clase Retweet

        Parámetros:
        - message (str):
        - sender (UserAccount):
        - tweet (Tweet):

        """
        super().__init__(message, sender)
        self.tweet = tweet

    def __str__(self):
        return f"Retweet from {self.sender.alias} at {self.time}: {self.message} | Original Tweet: {self.tweet}"



'''
Pregunta 1: 

    ¿Deberá modificar los atributos timeline y tweets de la clase UserAccount
    (definida en el ejercicio 1) para que contenga elementos de la clase hija Retweet?
    Justifique su razonamiento y, si cree que hay que modificarlos, explique también cómo lo haría.
    
Respuesta 1: 

    No, no sería necesario modificar los atributos timeline y tweets de la clase UserAccount 
    para que contengan elementos de la clase hija Retweet.

    La razón es que, aunque Retweet es una clase hija de Tweet, los objetos Retweet aún son objetos Tweet. 
    Esto significa que los objetos Retweet pueden ser almacenados en las listas tweets y timeline sin necesidad 
    de modificar su tipo de datos.

    En Python, las listas pueden contener objetos de diferentes tipos, siempre y cuando sean subtipos de los 
    tipos esperados. En este caso, Retweet es un subtipo de Tweet, por lo que no hay ningún problema en almacenar 
    objetos Retweet en las listas tweets y timeline que están diseñadas para contener objetos Tweet.

    Por lo tanto, no sería necesario realizar modificaciones adicionales en la definición de los atributos timeline
    y tweets de la clase UserAccount. Los objetos Retweet se pueden agregar a estas listas sin problemas y seguirán 
    funcionando correctamente en el contexto de la clase UserAccount.

Pregunta 2:

    Sí, sería necesario modificar el método tweet de la clase UserAccount para que pueda enviar objetos de tipo Retweet.
    Esto se debe a que el método actualmente solo admite objetos de tipo Tweet y no considera la posibilidad de enviar 
    retweets.
    
    Para implementar esto deberia de hacerse estos cambios:  
'''
def tweet_actualizada_pregunta2(self, tweet1: Union[Tweet, Retweet]):

    self.tweets.append(tweet1)
    self.notify_followers(tweet1)

'''
    En este caso, hemos modificado el tipo del parámetro tweet1 utilizando la clase Union del módulo typing. 
    La clase Union nos permite especificar múltiples tipos posibles para un parámetro. 
    En este caso, estamos indicando que tweet1 puede ser tanto un objeto de tipo Tweet como un objeto de tipo Retweet.

    Con esta modificación, el método tweet podrá recibir tanto tweets normales como retweets y los añadirá 
    correctamente a la lista tweets del usuario. Además, se notificará a los seguidores del usuario sobre 
    el tweet o retweet publicado.

    Tambien se habrian de hacer estas modificaciones en las clases de notify_followers y recieve_followers
    para implementar el retweet a su pleno funcionamiento, de esta manera:
'''
def notify_followers_actualizada_pregunta2(self, tweet: Union[Tweet, Retweet]):

    for follower in self.followers:
        follower.receive_tweet(tweet)

def receive_tweet_actualizada_pregunta2(self, tweet: Union[Tweet, Retweet]):

    self.timeline.append(tweet)