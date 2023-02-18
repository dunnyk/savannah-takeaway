from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from helpers.serialization_errors import error_dict


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        allow_null=False,
        required=True,
        error_messages={
            'required': error_dict['required'],
            'invalid': error_dict['invalid_name'].format('First name')
        }
    )

    last_name = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        allow_null=False,
        required=True,
        error_messages={
            'required': error_dict['required'],
            'invalid': error_dict['invalid_name'].format('First name')
        }
    )

    email = serializers.EmailField(
        required=True,
        allow_null=False,  # the box for email field should not be empty
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=error_dict['already_exist'].format("Email"),
            )
        ],
        error_messages={
            'required': error_dict['required'],
        }
    )

    username = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        allow_null=False,
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=error_dict['already_exist'].format("Username"),
            )
        ],
        error_messages={
            'required': error_dict['required'],
            'invalid': error_dict['invalid_name'].format('Username')
        }
    )

    password = serializers.RegexField(
        regex=("^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*"),
        min_length=8,
        max_length=30,
        required=True,
        # you can't leave this slot empty. if was true, it means  no need for teh required.
        allow_null=False,
        # write only means you don't copy paste things there.
        write_only=True,
        error_messages={
            'required': error_dict['required'],
            'min_length': error_dict['min_length'].format("Password", "8"),
            'max_length': 'Password cannot be more than 30 characters',
            'invalid': error_dict['invalid_password'],
        }
    )

    phone_number = serializers.RegexField(
        regex='^(?:\B\+ ?254|\b0)(?: [(-]? *\d(?:[ \d]\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?',
        allow_null=False,
        required=True,
        min_length=10,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=error_dict['already_exist'].format("Phone number"),
            )
        ],
        error_messages={
            'required': error_dict['required'],
            'min_length': error_dict['min_length'].format("Phone number", "10"),
            'invalid': error_dict['invalid_phone_no']
        }
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number']


class LoginSerializer(serializers.Serializer):
    '''login serializer class'''
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    @staticmethod
    def validate(data):
        '''
            The `validate` method is where we make sure that the current
            instance of LoginSerializer is "valid". In the case of signing in a
            user, this means validating that they've provided an email
            and password and that this combination matches one of the users in
            our database.
        '''
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email is required to log in')

        if password is None:
            raise serializers.ValidationError(
                'A Password is required to log in')

        user = User.objects.filter(email=email, password=password).first()
        if user is None:
            raise serializers.ValidationError(
                'user with this email and password was not found')
        return {'email': user.email, 'token': user.token}


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number']