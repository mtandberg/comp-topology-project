class Matrix4 {
	public:
		float matrix[16];

	Matrix4(float initmatrix[16]){
		for (int i = 0; i < 16; i++) {
			matrix[i]=initmatrix[i];
		}
	}

	Matrix4() {
		float init[16] = {1, 0, 0, 0,
		       	0, 1, 0, 0, 
			0, 0, 1, 0, 
			0, 0, 0, 1};
                for (int i = 0; i < 16; i++)
                                {
                                matrix[i]=init[i];
                        }
                        //nothing to do
        }

    //destruct
        ~Matrix4() {
                //destruct
        }
};


//Scaling operation
Matrix4 operator*(Matrix4 m, float s) {

       float result[16]; 
       for(int i = 0; i < 16; i++){
               result[i] = s*m.matrix[i];
       }
       Matrix4 res(result);
       return res;
}

Matrix4 operator*(float s, Matrix4 m) {

       float result[16]; 
       for(int i = 0; i < 16; i++){
               result[i] = s*m.matrix[i];
       }
       Matrix4 res(result);
       return res;
}


Matrix4 operator*(Matrix4 m1, Matrix4 m2){
        float result[16];
       float first, second, third, fourth;
        for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                        first = m1.matrix[(4*i)]*m2.matrix[j];
                       second = m1.matrix[(4*i)+1]*m2.matrix[j+4];
                       third = m1.matrix[(4*i)+2]*m2.matrix[j+8];
		       fourth = m1.matrix[(4*i)+3]*m2.matrix[j+12];
                       result[(4*i)+j]=first+second+third+fourth;
                }
        }
        return Matrix4(result);
}


