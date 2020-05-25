from django import forms
# 파이썬코드를 html에 적용시켜줄 수 있음. 즉 html코드로 작성하던 것을 파이썬 코드로 작성
class BoardForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput( #input type text
            attrs={ #속성
                'class':'form-control',
                'placeholder':'제목',
                'required': True
            }
        )
    )

    author = forms.CharField(
        widget=forms.TextInput( #input type text
            attrs={ #속성
                'class':'form-control',
                'placeholder':'작성자',
                'required': True,
                'hidden':True
            }
        )
    )
    
    content = forms.CharField(
        widget=forms.Textarea( #textarea
            attrs={ #속성
                'class':'form-control',
                'placeholder':'내용',
                'required': True
            }
        )
    )
    #여기서 지정한 title이나 author 라는 이름 그대로 태그 name속성값이 저 title이나 author라는 이름으로 됨
