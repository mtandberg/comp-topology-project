#include <csci441/matrix.h>
#include <math.h>

class Scale : public Matrix3 {
	public: 

	Scale(float x, float y){
		float array[9] = {x, 0, 0, 0, y, 0, 0, 0, 1};
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=array[i];
		}

	}

	Scale(float s){
		float array[9] = {s, 0, 0, 0, s, 0, 0, 0, 1};
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=array[i];
		}

	}

	Scale(){
		float array[9] = {1, 0, 0, 0, 1, 0, 0, 0, 1};
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=array[i];
		}
	}

	~Scale(){

	}

};

class Translate : public Matrix3 
{
public:

	Translate(float x, float y){
		float array[9] = {1, 0, x, 0, 1, y, 0, 0, 1};
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=array[i];
		}

	}
	~Translate(){

	}
	
};

class Rotate : public Matrix3
{
public:
	Rotate(float theta){
		float array[9] = {cos(theta), -sin(theta), 0, 
			sin(theta), cos(theta), 0, 
			0, 0, 1};
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=array[i];
		}
	}
	~Rotate(){

	}
	
};