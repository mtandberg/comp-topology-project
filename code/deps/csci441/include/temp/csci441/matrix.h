#include <string>
#include <csci441/vector3.h>
#include <csci441/point.h>

class Matrix3 {
	public:
		float matrix[9];

	Matrix3(float initmatrix[9]) {
		for (int i = 0; i < 9; ++i)
		{
			matrix[i]=initmatrix[i];
		}
		//nothing to do
	}



	//Init to id. matrix
	Matrix3()  {
		float init[9] = {1, 0, 0, 0, 1, 0, 0, 0, 1};
		for (int i = 0; i < 9; ++i)
				{
				matrix[i]=init[i];
			}
			//nothing to do
	}

	//destruct
	~Matrix3() {
		//destruct
	}
};

//Scaling operation
Matrix3 operator*(Matrix3 m, float s) {

       float result[9]; 
       for(int i = 0; i < 9; i++){
	       result[i] = s*m.matrix[i];
       }
       result[8] = 1;
       Matrix3 res(result);
       return res;
}

Matrix3 operator*(float s, Matrix3 m) {
       float result[9]; 
       for(int i = 0; i < 9; i++){
	       result[i] = s*m.matrix[i];
       }
       result[8] = 1;
       Matrix3 res(result);
       return res;
}

//Matrix * Vector
Vector3 operator*(Matrix3 m, Vector3 v) {
       float result[3]; 
       float first, second, third;
       for(int i = 0; i < 3; i++){

	       first = m.matrix[(3*i)]*v.x;
	       second = m.matrix[(3*i)+1]*v.y;
	       third = m.matrix[(3*i)+2]*v.z;

	       result[i]=first+second+third;
	       
       }
       Vector3 res(result[0], result[1],result[2]);
	       
       return res;
}

//Matrix * point
Point operator*(Matrix3 m, Point p) {
       float result[3]; 
       float first, second, third;
       for(int i = 0; i < 3; i++){

	       first = m.matrix[(3*i)]*p.x;
	       second = m.matrix[(3*i)+1]*p.y;
	       third = m.matrix[(3*i)+2]*1;

	       result[i]=first+second+third;
	       
       }
       Point res(result[0], result[1],p.r, p.g, p.b);
	       
       return res;
}
Matrix3 operator*(Matrix3 m1, Matrix3 m2){
	float result[9];
       float first, second, third;
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			first = m1.matrix[(3*i)]*m2.matrix[j];
		       second = m1.matrix[(3*i)+1]*m2.matrix[j+3];
		       third = m1.matrix[(3*i)+2]*m2.matrix[j+6];
		       result[(3*i)+j]=first+second+third;
		}
	}
	return Matrix3(result);
}




			
