import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import authServices from "./authService";

const user = JSON.parse(localStorage.getItem("user"));

const initialState = {
  user: user ? user : null,
  isLoading: false,
  isError: false,
  isSuccess: false,
  message: "",
};

export const register = createAsyncThunk(
  "auth/register",
  async (userData, thunkapi) => {
    try {
      return await authServices.register(userData);
    } catch (err) {
      const message =
        (err.response && err.response.data && err.response.data.message) ||
        err.message;
      return thunkapi.rejectWithValue(message);
    }
  }
);

export const login = createAsyncThunk(
  "auth/login",
  async (userData, thunkapi) => {
    try {
      return await authServices.login(userData);
    } catch (err) {
      const message =
        (err.response && err.response.data && err.response.data.message) ||
        err.message;
      return thunkapi.rejectWithValue(message);
    }
  }
);

export const logout = createAsyncThunk("auth/logout", async () => {
  authServices.logout();
});

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    reset: (state) => {
      state.isError = false;
      state.isLoading = false;
      state.isSuccess = false;
      state.message = "";
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(register.pending, (state) => {
        state.isLoading = true;
      })

      .addCase(register.fulfilled, (state, action) => {
        state.isSuccess = true;
        state.isLoading = false;
      })
      .addCase(register.rejected, (state, action) => {
        state.isError = true;
        state.isLoading = false;
        state.user = null;
        state.message = action.payload;
      })

      // login
      .addCase(login.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.user = action.payload;
      })
      .addCase(login.rejected, (state, action) => {
        state.isError = true;
        state.isLoading = false;
        state.user = null;
        state.message = action.payload;
      })

      // logout
      .addCase(logout.fulfilled, (state) => {
        state.user = null;
      });
  },
});

export const { reset } = authSlice.actions;
export default authSlice.reducer;
