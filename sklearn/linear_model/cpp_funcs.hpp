
template <typename T>
T* array_new(int n) {
    return new T[n];
}

template <typename T>
void array_delete(T* n) {
    delete [] n;
}