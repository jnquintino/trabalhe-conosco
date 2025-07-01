import { validateCPF, validateCNPJ, validateCPFCNPJ, formatCPFCNPJ, validateAreas } from './validation';

describe('Validation Utils', () => {
  describe('validateCPF', () => {
    it('should validate a correct CPF', () => {
      expect(validateCPF('12345678909')).toBe(true);
    });

    it('should reject an invalid CPF', () => {
      expect(validateCPF('12345678900')).toBe(false);
    });

    it('should reject CPF with all same digits', () => {
      expect(validateCPF('11111111111')).toBe(false);
    });

    it('should reject CPF with wrong length', () => {
      expect(validateCPF('123456789')).toBe(false);
    });
  });

  describe('validateCNPJ', () => {
    it('should validate a correct CNPJ', () => {
      expect(validateCNPJ('11222333000181')).toBe(true);
    });

    it('should reject an invalid CNPJ', () => {
      expect(validateCNPJ('11222333000180')).toBe(false);
    });

    it('should reject CNPJ with all same digits', () => {
      expect(validateCNPJ('11111111111111')).toBe(false);
    });
  });

  describe('validateCPFCNPJ', () => {
    it('should validate a correct CPF', () => {
      expect(validateCPFCNPJ('12345678909')).toBe(true);
    });

    it('should validate a correct CNPJ', () => {
      expect(validateCPFCNPJ('11222333000181')).toBe(true);
    });

    it('should reject invalid values', () => {
      expect(validateCPFCNPJ('123456789')).toBe(false);
    });
  });

  describe('formatCPFCNPJ', () => {
    it('should format CPF correctly', () => {
      expect(formatCPFCNPJ('12345678909')).toBe('123.456.789-09');
    });

    it('should format CNPJ correctly', () => {
      expect(formatCPFCNPJ('11222333000181')).toBe('11.222.333/0001-81');
    });

    it('should return original value for invalid length', () => {
      expect(formatCPFCNPJ('123456789')).toBe('123456789');
    });
  });

  describe('validateAreas', () => {
    it('should validate correct areas', () => {
      expect(validateAreas(1000, 600, 400)).toBe(true);
    });

    it('should reject when sum exceeds total', () => {
      expect(validateAreas(1000, 600, 500)).toBe(false);
    });

    it('should accept when sum equals total', () => {
      expect(validateAreas(1000, 600, 400)).toBe(true);
    });
  });
}); 