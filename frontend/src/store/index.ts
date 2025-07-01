import { configureStore } from '@reduxjs/toolkit';
import produtoresReducer from './produtoresSlice';
import dashboardReducer from './dashboardSlice';

export const store = configureStore({
  reducer: {
    produtores: produtoresReducer,
    dashboard: dashboardReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch; 