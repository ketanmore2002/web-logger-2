from rest_framework import serializers
from .models import *


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = nodes_model
        # fields = ('id', 'machine', 'location', 'sub_location', 'humidity','tempreture','tempreture_low','tempreture_high','battery','user_name','delete_status','uuid','_uuid',"humidity_low","humidity_high","CO2_high","CO2_low","CO2",'updated_at','email')
        fields = '__all__' 





class voltageRSerializer(serializers.ModelSerializer):
    class Meta:
        model = voltageR_parameters
        fields = '__all__' 
class voltageYSerializer(serializers.ModelSerializer):
    class Meta:
        model = voltageY_parameters
        fields = '__all__' 
class voltageBSerializer(serializers.ModelSerializer):
    class Meta:
        model = voltageB_parameters
        fields = '__all__' 


class currentRSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentR_parameters
        fields = '__all__' 
class currentYSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentY_parameters
        fields = '__all__' 
class currentBSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentB_parameters
        fields = '__all__' 

class powerSerializer(serializers.ModelSerializer):
    class Meta:
        model = power_parameters
        fields = '__all__' 

class generator_speedSerializer(serializers.ModelSerializer):
    class Meta:
        model = generator_speed_parameters
        fields = '__all__' 

class windspeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = windspeed_parameters
        fields = '__all__' 

class torqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = torque_parameters
        fields = '__all__' 