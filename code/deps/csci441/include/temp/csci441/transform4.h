#include <csci441/matrix4.h>
#include <math.h>
#include <csci441/vector3.h>

class Scale : public Matrix4 {
	public: 

	Scale(float x, float y, float z){
		float array[16] = {x, 0, 0, 0,
		       0, y, 0, 0,
	       	       0, 0, z, 0, 
		       0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}

	}

	Scale(float s){
		float array[16] = {s, 0, 0, 0,
		       0, s, 0, 0,
	       	       0, 0, s, 0, 
		       0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}

	}


	~Scale(){

	}

};

class Translate : public Matrix4 
{
public:

	Translate(float x, float y, float z){
		float array[16] = {1, 0, 0, x,
		       	0, 1, 0, y,
		       	0, 0, 1, z,
		        0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}

	}
	~Translate(){

	}
	
};

class RotateX : public Matrix4
{
public:
	RotateX(float theta){
		float array[16] = {1, 0, 0, 0, 
			0, cos(theta), -sin(theta), 0, 
			0, sin(theta), cos(theta), 0,
			0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}
	}
	~RotateX(){

	}
	
};

class RotateZ : public Matrix4
{
public:
	RotateZ(float theta){
		float array[16] = {cos(theta), -sin(theta), 0, 0, 
			sin(theta), cos(theta), 0, 0,
			0, 0, 1, 0, 
			0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}
	}
	~RotateZ(){

	}
	
};

class RotateY : public Matrix4
{
public:
	RotateY(float theta){
		float array[16] = {cos(theta),0, sin(theta), 0, 
			0, 1, 0, 0,
			-sin(theta), 0, cos(theta), 0, 
			0, 0, 0, 1};
		for (int i = 0; i < 16; ++i)
		{
			matrix[i]=array[i];
		}
	}
	~RotateY(){

	}
	
};

class View : public Matrix4
{
	public:
		Vector3 w;
		Vector3 u;
		Vector3 v;
	View(Vector3 e, Vector3 g, Vector3 t){
		w = norm(e-g);
		u = norm(w^t);
		v = u^w;
		float init1[16] = {u.x, u.y, u.z, 0,
			v.x, v.y, v.z, 0,
			w.x, w.y, w.z, 0,
			0, 0, 0, 1};
		Matrix4 help(init1);
		float init2[16] = {1, 0, 0, -e.x,
			0, 1, 0, -e.y,
			0, 0, 1, -e.z,
			0, 0, 0, 1};
		Matrix4 help2(init2);
		Matrix4 result = help*help2;
		for(int i = 0; i < 16; i++){
			matrix[i] = result.matrix[i];
		}
	}

	~View(){
	}
};

class Orth : public Matrix4
{
	public:

	Orth(float right, float left, float top, float bottom, float far, float near){
		float init[16] = {2/(right-left), 0, 0, -(right+left)/(right-left),
			0, 2/(top-bottom), 0, -(top+bottom)/(top-bottom),
			0, 0, -2/(far-near), -(far+near)/(far-near),
			0,0,0,1};
		for(int i = 0; i < 16; i++){
			matrix[i] = init[i];
		}
			
	}
};

class Perspective : public Matrix4
{
	public:
	Perspective(float FOV, float aspect, float far, float near){
		/*
	
		float top = near*tan(3.14*FOV/360);
		float bottom = -top;
		float right = top*aspect;
		float left = -right;
		*/
		float mid = tan(FOV*3.14/360);
		float init[16] = 
		{1/mid, 0, 0, 0,
			0, 1/mid, 0, 0,
			0, 0, -far/(far-near), -1,
			0, 0, -far*near/(far-near), 0
		};
		for(int i = 0; i < 16; i++){
			matrix[i] = init[i];
		}
	}
};

		
