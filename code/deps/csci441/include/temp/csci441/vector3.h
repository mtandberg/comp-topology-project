#include <math.h>
class Vector3 {



	public:

    	float x;

	float y;

    	float z;



	// Constructor

	Vector3(float xx, float yy, float zz) : x(xx), y(yy), z(zz) {

		// nothing to do here as we've already initialized x, y, and z above

		//std::cout << "in Vector3 constructor" << std::endl;

	}


	
		

	Vector3() : x(0), y(0), z(0) {//default is <0,0,0>



	}



	// Destructor - called when an object goes out of scope or is destroyed

	~Vector3() {

		//this is where you would release resources such as memory or file descriptors

		// in this case we don't need to do anything

		//std::cout << "in Vector3 destructor" << std::endl;

	}



	

		

};



Vector3 add(const Vector3& v, const Vector3& v2) { 

	Vector3 result = Vector3(v.x+v2.x, v.y+v2.y, v.z+v2.z);

	return result;

}

std::ostream& operator<<(std::ostream& stream, const Vector3& v) {

    // std::cout is a std::ostream object, just like stream

    // so use stream as if it were cout and output the components of

    // the vector

       

	stream << "<" << v.x << "," << v.y << "," << v.z << ">";

	return stream;

}

Vector3 operator+(const Vector3& v, const Vector3& v2) { 

	Vector3 result = Vector3(v.x+v2.x, v.y+v2.y, v.z+v2.z);

	return result;

}
Vector3 operator-(Vector3 v){
	return Vector3(-v.x, -v.y, -v.z);
}





Vector3 operator*(Vector3 v, float s) { 

	Vector3 result = Vector3(v.x*s,v.y*s, v.z*s);

	return result;

}





Vector3 operator*(float s, Vector3 v) { 

	Vector3 result = Vector3(v.x*s,v.y*s, v.z*s);

	return result;

}
float operator*(Vector3 v1, Vector3 v2){
	return (v1.x*v2.x + v1.y*v2.y + v1.z*v2.z);
}

Vector3 operator^(Vector3 v1, Vector3 v2){
	float first = v1.y*v2.z - v1.z*v2.y;
	float second = -v1.x*v2.z + v1.z*v2.x;
	float third = v1.x*v2.y - v1.y*v2.x;
	Vector3 result = Vector3(first, second, third);
	return result;
}
Vector3 operator-(Vector3 v1, Vector3 v2){
	return Vector3(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z);
}


Vector3 norm(Vector3 v){
	float mag = sqrt(v*v);
	return Vector3(v.x/mag, v.y/mag, v.z/mag);
}
