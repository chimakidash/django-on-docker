from django import forms
from .models import Post, Player, Card

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PlayerForm(forms.ModelForm):
   class Meta:
       model = Player
       fields=(
           'name',
           'HP',
           'point',
           )
       labels = [
           {'name':'プレイヤー名'},
           {'HP':'ライフ'},
           {'point':'得点'},
           ]

class CardForm(forms.ModelForm):
   class Meta:
       model=Card
       fields =(
           'element',
           'num',
           )
       labels= [
           {'element':'属性'},
           {'num':'数'},
           ]