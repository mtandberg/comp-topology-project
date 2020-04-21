
class Point {
    public:
	    float x;
	    float y;
	    float r;
	    float g;
	    float b;
    //Constructor
    Point(float xx, float yy, float rr, float gg, float bb) : x(xx), y(yy), r(rr), g(gg), b(bb) {
	    //nothing to do
	    //std::cout << "In point constructor" << std::endl;
    }

    //default
    Point() : x(0), y(0), r(1), g(1), b(1) {
    }
    ~Point(){
	    //std::cout << "Destructing point" <<std::endl;
    }
};

std::ostream& operator<<(std::ostream& stream, const Point& p){
    stream << "<" << p.x << "," << p.y << ">";
    return stream;
}